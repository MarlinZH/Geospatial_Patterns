"""
Geospatial Patterns Analyzer
A tool for analyzing spatial patterns and proximity relationships of geographic entities.
"""

import geopandas as gpd
from shapely.geometry import Point, Polygon
import osmnx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import BallTree
from typing import Dict, Tuple, Optional
import warnings

warnings.filterwarnings('ignore')


class GeospatialAnalyzer:
    """
    A class for analyzing geospatial patterns of entities in a specified area.
    
    Attributes:
        area (str): Location name searchable on OpenStreetMap
        tags (dict): OSM tags for filtering entities (e.g., {"shop": "convenience"})
        walking_radius_meters (float): Proximity radius in meters for neighbor search
        output_verbose (bool): Whether to print detailed outputs
        leaf_size (int): BallTree leaf size parameter for optimization
    """
    
    EARTH_RADIUS_METERS = 6371000  # Earth's radius in meters
    
    def __init__(
        self,
        area: str,
        tags: Dict[str, str],
        walking_radius_meters: float = 168,
        output_verbose: bool = False,
        leaf_size: int = 15
    ):
        """
        Initialize the GeospatialAnalyzer.
        
        Args:
            area: Location name (e.g., "Shinjuku, Tokyo")
            tags: OSM tags dictionary (e.g., {"shop": "convenience"})
            walking_radius_meters: Proximity search radius in meters (default: 168m ≈ 2 min walk)
            output_verbose: Print detailed outputs (default: False)
            leaf_size: BallTree optimization parameter (default: 15)
        """
        self.area = area
        self.tags = tags
        self.walking_radius_meters = walking_radius_meters
        self.output_verbose = output_verbose
        self.leaf_size = leaf_size
        
        # Cache for computed values
        self._boundaries = None
        self._entities_df = None
        self._tree = None
        
    def _get_area_boundaries(self) -> Tuple[float, float, float, float, any]:
        """
        Get the geographic boundaries of the specified area.
        
        Returns:
            Tuple of (north, south, east, west, location_polygon)
        """
        if self._boundaries is not None:
            return self._boundaries
            
        try:
            gdf = osmnx.geocode_to_gdf(self.area)
            bounding = gdf.bounds
            
            north = bounding.iloc[0, 3]
            south = bounding.iloc[0, 1]
            east = bounding.iloc[0, 2]
            west = bounding.iloc[0, 0]
            location = gdf.unary_union
            
            self._boundaries = (north, south, east, west, location)
            
            if self.output_verbose:
                print(f"Area boundaries retrieved for: {self.area}")
                print(f"North: {north:.4f}, South: {south:.4f}")
                print(f"East: {east:.4f}, West: {west:.4f}")
                
            return self._boundaries
            
        except Exception as e:
            raise ValueError(f"Could not geocode area '{self.area}': {str(e)}")
    
    def get_entities_list(self, force_refresh: bool = False) -> pd.DataFrame:
        """
        Retrieve a list of entities from OpenStreetMap matching the specified tags.
        
        Args:
            force_refresh: If True, bypass cache and fetch fresh data
            
        Returns:
            DataFrame with columns: OSM Tag, Brand, longitude, latitude
        """
        if self._entities_df is not None and not force_refresh:
            return self._entities_df
            
        north, south, east, west, location = self._get_area_boundaries()
        
        try:
            # Fetch entities from OSM
            entities = osmnx.geometries_from_bbox(north, south, east, west, self.tags)
            
            # Set coordinate reference system
            entities = entities.set_crs(4326)
            
            # Filter entities within the location polygon
            entities = entities[entities.geometry.within(location)]
            
            # Convert polygons to centroids
            entities['geometry'] = entities['geometry'].apply(
                lambda x: x.centroid if isinstance(x, Polygon) else x
            )
            
            # Filter to keep only Point geometries
            entities = entities[entities.geom_type == 'Point']
            
            # Create clean DataFrame
            entities_list = pd.DataFrame({
                'OSM Tag': list(self.tags.values())[0],
                'Brand': entities.get('brand:en', entities.get('name', 'Unknown')).tolist(),
                'longitude': entities['geometry'].x.tolist(),
                'latitude': entities['geometry'].y.tolist()
            })
            
            # Remove entries without brand information
            entities_list = entities_list[entities_list['Brand'].notna()]
            
            self._entities_df = entities_list
            
            if self.output_verbose:
                print(f"\nEntities successfully retrieved: {len(entities_list)} locations")
                print(f"Unique brands: {entities_list['Brand'].nunique()}")
                
            return entities_list
            
        except Exception as e:
            raise RuntimeError(f"Error fetching entities: {str(e)}")
    
    def get_entity_counts(self) -> pd.Series:
        """
        Get count of entities by brand/name.
        
        Returns:
            Series with brand names as index and counts as values
        """
        entities = self.get_entities_list()
        counts = entities['Brand'].value_counts()
        
        if self.output_verbose:
            print("\nEntity counts by brand:")
            print(counts)
            
        return counts
    
    def analyze_proximity(self, return_distances: bool = False) -> pd.DataFrame:
        """
        Analyze proximity relationships between entities.
        
        Args:
            return_distances: If True, include distances in the output
            
        Returns:
            DataFrame with neighboring entities within walking radius
        """
        entities = self.get_entities_list()
        
        # Convert coordinates to radians for haversine distance
        locations = entities[["latitude", "longitude"]].values
        locations_radians = np.radians(locations)
        
        # Create BallTree for efficient neighbor search
        if self._tree is None:
            self._tree = BallTree(
                locations_radians,
                leaf_size=self.leaf_size,
                metric='haversine'
            )
        
        # Query radius in radians
        radius_radians = self.walking_radius_meters / self.EARTH_RADIUS_METERS
        
        # Find neighbors within radius
        indices, distances = self._tree.query_radius(
            locations_radians,
            r=radius_radians,
            return_distance=True
        )
        
        # Create DataFrame with results
        proximity_df = pd.DataFrame({
            'Entity': entities['Brand'].values,
            'Location': list(zip(entities['latitude'], entities['longitude'])),
            'Neighbors': [
                [entities.iloc[idx]['Brand'] for idx in neighbor_indices if idx != i]
                for i, neighbor_indices in enumerate(indices)
            ],
            'Neighbor_Count': [len(neighbor_indices) - 1 for neighbor_indices in indices]
        })
        
        if return_distances:
            proximity_df['Distances_m'] = [
                [dist * self.EARTH_RADIUS_METERS for j, dist in enumerate(neighbor_dists) 
                 if neighbor_indices[j] != i]
                for i, (neighbor_indices, neighbor_dists) in enumerate(zip(indices, distances))
            ]
        
        if self.output_verbose:
            print(f"\nProximity analysis complete:")
            print(f"Search radius: {self.walking_radius_meters}m")
            print(f"Average neighbors per entity: {proximity_df['Neighbor_Count'].mean():.2f}")
            print(f"Max neighbors for any entity: {proximity_df['Neighbor_Count'].max()}")
            
        return proximity_df
    
    def visualize_distribution(
        self,
        save_path: Optional[str] = None,
        top_n: Optional[int] = None,
        figsize: Tuple[int, int] = (10, 8)
    ):
        """
        Create a pie chart visualization of entity distribution.
        
        Args:
            save_path: If provided, save the figure to this path
            top_n: If provided, only show top N brands (others grouped as "Other")
            figsize: Figure size as (width, height) tuple
        """
        counts = self.get_entity_counts()
        
        # Group smaller brands if top_n is specified
        if top_n and len(counts) > top_n:
            top_counts = counts.head(top_n)
            other_count = counts.iloc[top_n:].sum()
            if other_count > 0:
                top_counts['Other'] = other_count
            counts = top_counts
        
        # Create pie chart
        plt.figure(figsize=figsize)
        plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f'Entity Distribution in {self.area}\n({list(self.tags.keys())[0]}: {list(self.tags.values())[0]})')
        plt.axis('equal')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            if self.output_verbose:
                print(f"\nVisualization saved to: {save_path}")
        
        plt.show()
    
    def export_to_csv(self, entities_path: str = "entities.csv", proximity_path: str = "proximity.csv"):
        """
        Export analysis results to CSV files.
        
        Args:
            entities_path: Path for entities CSV file
            proximity_path: Path for proximity analysis CSV file
        """
        entities = self.get_entities_list()
        proximity = self.analyze_proximity()
        
        entities.to_csv(entities_path, index=False)
        
        # Flatten proximity data for CSV export
        proximity_export = proximity[['Entity', 'Neighbor_Count']].copy()
        proximity_export['Neighbors'] = proximity['Neighbors'].apply(lambda x: ', '.join(x))
        proximity_export.to_csv(proximity_path, index=False)
        
        if self.output_verbose:
            print(f"\nData exported:")
            print(f"  Entities: {entities_path}")
            print(f"  Proximity: {proximity_path}")


def main():
    """
    Example usage of the GeospatialAnalyzer.
    """
    print("=" * 70)
    print("Geospatial Patterns Analyzer")
    print("=" * 70)
    
    # Configure analysis parameters
    config = {
        'area': 'Shinjuku, Tokyo',
        'tags': {"shop": "convenience"},
        'walking_radius_meters': 168,  # ~2 minute walk
        'output_verbose': True
    }
    
    # Initialize analyzer
    print(f"\nInitializing analyzer for: {config['area']}")
    print(f"Entity type: {config['tags']}")
    print(f"Walking radius: {config['walking_radius_meters']}m")
    
    analyzer = GeospatialAnalyzer(**config)
    
    # Get entity counts
    print("\n" + "=" * 70)
    print("ENTITY ANALYSIS")
    print("=" * 70)
    counts = analyzer.get_entity_counts()
    
    # Analyze proximity
    print("\n" + "=" * 70)
    print("PROXIMITY ANALYSIS")
    print("=" * 70)
    proximity = analyzer.analyze_proximity(return_distances=False)
    print("\nSample proximity results (first 5 entities):")
    print(proximity[['Entity', 'Neighbor_Count', 'Neighbors']].head())
    
    # Create visualization
    print("\n" + "=" * 70)
    print("VISUALIZATION")
    print("=" * 70)
    analyzer.visualize_distribution(top_n=10)
    
    # Export results
    print("\n" + "=" * 70)
    print("EXPORT")
    print("=" * 70)
    analyzer.export_to_csv()
    
    print("\n" + "=" * 70)
    print("Analysis complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
