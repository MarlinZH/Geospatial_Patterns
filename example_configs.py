"""
Example configurations for GeospatialAnalyzer

This file contains example configurations for different analysis scenarios.
Copy and modify these examples to suit your needs.
"""

# Example 1: Convenience stores in Tokyo
TOKYO_CONVENIENCE = {
    'area': 'Shinjuku, Tokyo',
    'tags': {"shop": "convenience"},
    'walking_radius_meters': 168,  # ~2 minute walk
    'output_verbose': True
}

# Example 2: Restaurants in New York
NYC_RESTAURANTS = {
    'area': 'Manhattan, New York',
    'tags': {"amenity": "restaurant"},
    'walking_radius_meters': 400,  # ~5 minute walk
    'output_verbose': True
}

# Example 3: Coffee shops in Seattle
SEATTLE_CAFES = {
    'area': 'Seattle, Washington',
    'tags': {"amenity": "cafe"},
    'walking_radius_meters': 250,  # ~3 minute walk
    'output_verbose': False
}

# Example 4: Banks in London
LONDON_BANKS = {
    'area': 'City of London, UK',
    'tags': {"amenity": "bank"},
    'walking_radius_meters': 500,  # ~6 minute walk
    'output_verbose': True
}

# Example 5: Pharmacies in Paris
PARIS_PHARMACIES = {
    'area': 'Paris, France',
    'tags': {"amenity": "pharmacy"},
    'walking_radius_meters': 300,  # ~3.5 minute walk
    'output_verbose': True
}

# Example 6: Supermarkets in Berlin
BERLIN_SUPERMARKETS = {
    'area': 'Berlin, Germany',
    'tags': {"shop": "supermarket"},
    'walking_radius_meters': 600,  # ~7 minute walk
    'output_verbose': True
}

# Example 7: Transit stations in Chicago
CHICAGO_TRANSIT = {
    'area': 'Chicago, Illinois',
    'tags': {"public_transport": "station"},
    'walking_radius_meters': 800,  # ~10 minute walk
    'output_verbose': True
}

# Example 8: Hotels in Las Vegas
VEGAS_HOTELS = {
    'area': 'Las Vegas, Nevada',
    'tags': {"tourism": "hotel"},
    'walking_radius_meters': 1000,  # ~12 minute walk
    'output_verbose': True
}

# Example 9: Custom neighborhood analysis
CUSTOM_CONFIG = {
    'area': 'Your Area Name Here',
    'tags': {"your_tag": "your_value"},  # See OSM Wiki for available tags
    'walking_radius_meters': 200,  # Adjust to your needs
    'output_verbose': True,
    'leaf_size': 15  # BallTree optimization parameter
}


def get_config(name: str) -> dict:
    """
    Get a configuration by name.
    
    Args:
        name: Configuration name (e.g., 'TOKYO_CONVENIENCE')
        
    Returns:
        Configuration dictionary
        
    Example:
        >>> config = get_config('NYC_RESTAURANTS')
        >>> analyzer = GeospatialAnalyzer(**config)
    """
    configs = {
        'TOKYO_CONVENIENCE': TOKYO_CONVENIENCE,
        'NYC_RESTAURANTS': NYC_RESTAURANTS,
        'SEATTLE_CAFES': SEATTLE_CAFES,
        'LONDON_BANKS': LONDON_BANKS,
        'PARIS_PHARMACIES': PARIS_PHARMACIES,
        'BERLIN_SUPERMARKETS': BERLIN_SUPERMARKETS,
        'CHICAGO_TRANSIT': CHICAGO_TRANSIT,
        'VEGAS_HOTELS': VEGAS_HOTELS,
        'CUSTOM': CUSTOM_CONFIG
    }
    
    if name not in configs:
        raise ValueError(f"Configuration '{name}' not found. Available: {list(configs.keys())}")
    
    return configs[name].copy()


# Walking speed reference (for calculating walking_radius_meters)
# Average adult walking speeds:
# - Slow walk: 1.0 m/s (3.6 km/h)
# - Normal walk: 1.4 m/s (5.0 km/h) ← default reference
# - Brisk walk: 1.8 m/s (6.5 km/h)
# - Fast walk: 2.2 m/s (8.0 km/h)
#
# Formula: walking_radius_meters = speed_m_per_s × time_seconds
# Example: For 5-minute normal walk = 1.4 × (5 × 60) = 420 meters


if __name__ == "__main__":
    # Print all available configurations
    print("Available Configurations:")
    print("=" * 70)
    
    configs = [
        ('TOKYO_CONVENIENCE', TOKYO_CONVENIENCE),
        ('NYC_RESTAURANTS', NYC_RESTAURANTS),
        ('SEATTLE_CAFES', SEATTLE_CAFES),
        ('LONDON_BANKS', LONDON_BANKS),
        ('PARIS_PHARMACIES', PARIS_PHARMACIES),
        ('BERLIN_SUPERMARKETS', BERLIN_SUPERMARKETS),
        ('CHICAGO_TRANSIT', CHICAGO_TRANSIT),
        ('VEGAS_HOTELS', VEGAS_HOTELS),
    ]
    
    for name, config in configs:
        print(f"\n{name}:")
        print(f"  Area: {config['area']}")
        print(f"  Tags: {config['tags']}")
        print(f"  Walking Radius: {config['walking_radius_meters']}m")
