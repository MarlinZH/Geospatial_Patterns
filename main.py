"""
Geospatial Patterns - Main Script
Example usage of the GeospatialAnalyzer class

This script demonstrates the basic functionality of analyzing spatial patterns
of convenience stores in Shinjuku, Tokyo.
"""

from geospatial_analysis import GeospatialAnalyzer


def main():
    """
    Main function demonstrating the GeospatialAnalyzer usage.
    """
    print("=" * 70)
    print("Geospatial Patterns Analyzer - Example Analysis")
    print("=" * 70)
    
    # Configure analysis parameters
    config = {
        'area': 'Shinjuku, Tokyo',
        'tags': {"shop": "convenience"},
        'walking_radius_meters': 168,  # approximately 2 minutes walking distance
        'output_verbose': True
    }
    
    # Initialize the analyzer
    print(f"\nAnalyzing: {config['area']}")
    print(f"Entity Type: {list(config['tags'].keys())[0]} = {list(config['tags'].values())[0]}")
    print(f"Walking Radius: {config['walking_radius_meters']} meters")
    
    analyzer = GeospatialAnalyzer(**config)
    
    # Perform entity analysis
    print("\n" + "=" * 70)
    print("STEP 1: ENTITY COUNT ANALYSIS")
    print("=" * 70)
    entity_counts = analyzer.get_entity_counts()
    
    # Perform proximity analysis
    print("\n" + "=" * 70)
    print("STEP 2: PROXIMITY ANALYSIS")
    print("=" * 70)
    proximity_results = analyzer.analyze_proximity(return_distances=False)
    
    # Display sample results
    print("\nSample Results (First 5 entities):")
    print("-" * 70)
    sample = proximity_results[['Entity', 'Neighbor_Count', 'Neighbors']].head()
    for idx, row in sample.iterrows():
        print(f"\n{row['Entity']}:")
        print(f"  - Neighbors within {config['walking_radius_meters']}m: {row['Neighbor_Count']}")
        if row['Neighbor_Count'] > 0:
            print(f"  - Nearby stores: {', '.join(row['Neighbors'][:3])}" + 
                  ("..." if len(row['Neighbors']) > 3 else ""))
    
    # Generate visualization
    print("\n" + "=" * 70)
    print("STEP 3: VISUALIZATION")
    print("=" * 70)
    print("Generating pie chart...")
    analyzer.visualize_distribution(top_n=10, save_path="entity_distribution.png")
    
    # Export results to CSV
    print("\n" + "=" * 70)
    print("STEP 4: EXPORT RESULTS")
    print("=" * 70)
    analyzer.export_to_csv(
        entities_path="entities_list.csv",
        proximity_path="proximity_analysis.csv"
    )
    
    # Summary statistics
    print("\n" + "=" * 70)
    print("SUMMARY STATISTICS")
    print("=" * 70)
    print(f"Total entities found: {len(proximity_results)}")
    print(f"Unique brands: {entity_counts.count()}")
    print(f"Most common brand: {entity_counts.index[0]} ({entity_counts.iloc[0]} locations)")
    print(f"Average neighbors per location: {proximity_results['Neighbor_Count'].mean():.2f}")
    print(f"Maximum neighbors for any location: {proximity_results['Neighbor_Count'].max()}")
    
    # Find locations with most neighbors (highest clustering)
    top_clustered = proximity_results.nlargest(3, 'Neighbor_Count')[['Entity', 'Neighbor_Count']]
    print("\nMost clustered locations:")
    for idx, row in top_clustered.iterrows():
        print(f"  - {row['Entity']}: {row['Neighbor_Count']} neighbors")
    
    print("\n" + "=" * 70)
    print("Analysis Complete!")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - entity_distribution.png")
    print("  - entities_list.csv")
    print("  - proximity_analysis.csv")
    print("\n")


if __name__ == "__main__":
    main()
