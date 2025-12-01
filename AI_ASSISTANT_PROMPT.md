# Geospatial Patterns - AI Assistant Prompt

Use this prompt when asking AI assistants to help you work with the Geospatial Patterns repository.

## Quick Start Prompt

```
I'm working with a geospatial analysis tool that analyzes spatial patterns and proximity relationships using OpenStreetMap data. The repository is at: https://github.com/MarlinZH/Geospatial_Patterns

Key information:
- Main class: GeospatialAnalyzer in geospatial_analysis.py
- Example usage: See main.py and example_configs.py
- Technologies: Python, geopandas, osmnx, shapely, scikit-learn

Current configurable parameters:
- area (str, required): Location name searchable on OpenStreetMap
- tags (dict, required): OSM tag filters (e.g., {"shop": "convenience"})
- walking_radius_meters (float, default: 168): Proximity search radius in meters
- output_verbose (bool, default: False): Print detailed outputs
- leaf_size (int, default: 15): BallTree optimization parameter

[Your specific question or task here]
```

## Detailed Context Prompt

```
I'm working with the Geospatial Patterns Python project for analyzing spatial patterns of geographic entities using OpenStreetMap data.

## Project Overview
Repository: https://github.com/MarlinZH/Geospatial_Patterns

This tool analyzes spatial patterns and proximity relationships between points of interest (POIs) in any geographic area. It uses OpenStreetMap data to:
- Extract geographic entities based on custom tags
- Analyze proximity relationships using BallTree algorithm
- Generate visualizations and export data

## Technical Stack
- Python 3.8+
- geopandas >= 0.14.0
- osmnx >= 1.9.0
- shapely >= 2.0.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- scikit-learn >= 1.3.0

## Core Components

### GeospatialAnalyzer Class (geospatial_analysis.py)
Main class with these parameters:
- area (str): Location name (e.g., "Shinjuku, Tokyo")
- tags (dict): OSM tags (e.g., {"shop": "convenience"})
- walking_radius_meters (float): Proximity radius in meters (default: 168)
- output_verbose (bool): Verbose output flag (default: False)
- leaf_size (int): BallTree parameter (default: 15)

### Key Methods
- get_entities_list(): Retrieve entities from OSM
- get_entity_counts(): Count entities by brand/name
- analyze_proximity(): Find neighbors within walking radius
- visualize_distribution(): Create pie chart visualization
- export_to_csv(): Export results to CSV files

## Common OSM Tags
- Shops: {"shop": "convenience"}, {"shop": "supermarket"}
- Amenities: {"amenity": "restaurant"}, {"amenity": "cafe"}
- Transit: {"public_transport": "station"}

Full list: https://wiki.openstreetmap.org/wiki/Map_Features

## Example Usage
```python
from geospatial_analysis import GeospatialAnalyzer

analyzer = GeospatialAnalyzer(
    area="Manhattan, New York",
    tags={"amenity": "restaurant"},
    walking_radius_meters=400,
    output_verbose=True
)

counts = analyzer.get_entity_counts()
proximity = analyzer.analyze_proximity()
analyzer.visualize_distribution(top_n=10)
analyzer.export_to_csv()
```

## Current Status
✅ Production-ready with proper documentation and modular code
⚠️ Needs repository cleanup (cache files, IDE folders)
📋 Outstanding: Testing, CLI interface, interactive maps

## My Question/Task
[Describe your specific question, bug report, or feature request here]
```

## Specific Use Case Prompts

### For Bug Reports
```
I'm experiencing an issue with the Geospatial Patterns tool (https://github.com/MarlinZH/Geospatial_Patterns).

**Context:**
- Using GeospatialAnalyzer class from geospatial_analysis.py
- Python version: [your version]
- Operating System: [your OS]

**Configuration:**
- area: "[your area]"
- tags: {your tags}
- walking_radius_meters: [your radius]

**Expected behavior:**
[What you expected to happen]

**Actual behavior:**
[What actually happened]

**Error message (if any):**
```
[paste error here]
```

**Steps to reproduce:**
1. [First step]
2. [Second step]
3. [etc.]
```

### For Feature Requests
```
I'd like to propose a new feature for the Geospatial Patterns tool (https://github.com/MarlinZH/Geospatial_Patterns).

**Current Functionality:**
The tool currently uses the GeospatialAnalyzer class to [describe current state].

**Proposed Feature:**
[Describe the feature you want]

**Use Case:**
[Explain why this feature would be useful]

**Potential Implementation:**
[Optional: Your ideas on how this could be implemented]

**Example Usage:**
```python
# How the feature might be used
```

**Related to:**
- Existing parameters: [list relevant parameters]
- Similar features: [mention any similar functionality]
```

### For Analysis Help
```
I'm using the Geospatial Patterns tool to analyze [your entity type] in [your area].

**My Setup:**
```python
from geospatial_analysis import GeospatialAnalyzer

analyzer = GeospatialAnalyzer(
    area="[your area]",
    tags={"[tag_key]": "[tag_value]"},
    walking_radius_meters=[your radius],
    output_verbose=True
)
```

**What I'm trying to do:**
[Describe your analysis goal]

**Current results:**
[What you've found so far]

**Questions:**
1. [Your question 1]
2. [Your question 2]
```

### For Configuration Help
```
I need help configuring the GeospatialAnalyzer for my use case.

**My Goal:**
Analyze [entity type] in [location] to [your objective]

**Questions:**
- What OSM tags should I use for [entity type]?
- What walking_radius_meters value makes sense for [scenario]?
- Should I enable output_verbose?

**Additional Context:**
[Any other relevant information]
```

## Pro Tips for AI Assistants

When working with this repository:

1. **Always check** the example_configs.py file for pre-built configurations
2. **Refer to** the OSM Wiki (https://wiki.openstreetmap.org/wiki/Map_Features) for tag options
3. **Remember** that walking_radius_meters is calculated as: speed_m_per_s × time_seconds
4. **Note** that the default walking speed is 1.4 m/s (5 km/h)
5. **Be aware** that cache files are stored locally and excluded from git
6. **Check** requirements.txt for exact package versions

## Walking Distance Quick Reference

| Time (minutes) | Radius (meters) | Use Case |
|----------------|-----------------|----------|
| 1 | 84 | Very close proximity |
| 2 | 168 | Default, quick walk |
| 3 | 250 | Short walk |
| 5 | 420 | Moderate walk |
| 10 | 840 | Extended walk |
| 15 | 1260 | Long walk |

## Common Issues & Solutions

1. **Import Error**: Check that Point and Polygon are capitalized in imports
2. **No Results**: Verify the area name is searchable on OpenStreetMap
3. **Missing Brands**: Some OSM entities may not have `brand:en` tags
4. **Slow Performance**: Reduce the area size or increase leaf_size parameter
5. **Connection Error**: Ensure internet connection for OSM API access

---

**Repository URL**: https://github.com/MarlinZH/Geospatial_Patterns
**Documentation**: See README.md in the repository
**Examples**: See example_configs.py for 8 pre-built configurations
