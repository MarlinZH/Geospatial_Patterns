# Geospatial Patterns

A Python tool for analyzing spatial patterns and proximity relationships of geographic entities using OpenStreetMap data. This project helps identify clusters, proximity networks, and spatial distributions of points of interest (POIs) in any given area.

## 🎯 Features

- **Entity Extraction**: Retrieve geographic entities from OpenStreetMap based on custom tags
- **Spatial Analysis**: Analyze proximity relationships between entities using BallTree algorithm
- **Visualization**: Generate pie charts and proximity network visualizations
- **Configurable Parameters**: Customize search areas, entity types, walking distances, and more
- **Brand Distribution**: Count and analyze brand/entity distributions in a given area

## 📋 Use Cases

- **Retail Analysis**: Analyze convenience store distributions and competitive proximity
- **Urban Planning**: Study spatial patterns of amenities, facilities, or services
- **Market Research**: Identify clusters and gaps in service coverage
- **Accessibility Studies**: Measure walking-distance relationships between locations

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MarlinZH/Geospatial_Patterns.git
cd Geospatial_Patterns
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start

Run the example analysis:
```bash
python main.py
```

This will analyze convenience stores in Shinjuku, Tokyo and generate:
- Entity count by brand
- Pie chart visualization
- Proximity network (stores within 2-minute walking distance)

## 📖 Usage

### Basic Usage

```python
from geospatial_analysis import GeospatialAnalyzer

# Initialize analyzer
analyzer = GeospatialAnalyzer(
    area="Shinjuku, Tokyo",
    tags={"shop": "convenience"},
    walking_radius_meters=168  # ~2 minute walk
)

# Get entity counts
counts = analyzer.get_entity_counts()

# Get proximity relationships
proximity = analyzer.analyze_proximity()

# Generate visualizations
analyzer.visualize_distribution()
```

### Advanced Usage

#### Analyze Different Entity Types

```python
# Analyze restaurants
analyzer = GeospatialAnalyzer(
    area="Manhattan, New York",
    tags={"amenity": "restaurant"}
)

# Analyze cafes
analyzer = GeospatialAnalyzer(
    area="Paris, France",
    tags={"amenity": "cafe"}
)

# Analyze pharmacies
analyzer = GeospatialAnalyzer(
    area="London, UK",
    tags={"amenity": "pharmacy"}
)
```

#### Custom Walking Distance

```python
# 5-minute walking radius (~420 meters at average walking speed)
analyzer = GeospatialAnalyzer(
    area="Downtown Seattle",
    tags={"shop": "supermarket"},
    walking_radius_meters=420
)
```

#### Export Results

```python
# Get entity list as DataFrame
entities_df = analyzer.get_entities_list()
entities_df.to_csv("entities.csv", index=False)

# Get proximity network
proximity_df = analyzer.analyze_proximity()
proximity_df.to_csv("proximity_network.csv", index=False)
```

## 🔧 Configuration

### Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `area` | str | Location name (searchable on OSM) | Required |
| `tags` | dict | OSM tag filters (e.g., `{"shop": "convenience"}`) | Required |
| `walking_radius_meters` | int/float | Proximity radius in meters | 168 |
| `output_verbose` | bool | Print detailed outputs | False |
| `leaf_size` | int | BallTree leaf size for optimization | 15 |

### Common OSM Tags

**Shops**:
- `{"shop": "convenience"}` - Convenience stores
- `{"shop": "supermarket"}` - Supermarkets
- `{"shop": "bakery"}` - Bakeries
- `{"shop": "clothes"}` - Clothing stores

**Amenities**:
- `{"amenity": "restaurant"}` - Restaurants
- `{"amenity": "cafe"}` - Cafes
- `{"amenity": "bank"}` - Banks
- `{"amenity": "pharmacy"}` - Pharmacies
- `{"amenity": "hospital"}` - Hospitals

**Transportation**:
- `{"public_transport": "station"}` - Transit stations
- `{"amenity": "parking"}` - Parking facilities

For more tags, visit the [OSM Tag Wiki](https://wiki.openstreetmap.org/wiki/Map_Features).

## 📊 Output Examples

### Entity Count Output
```
Brand
7-Eleven        45
FamilyMart      38
Lawson          32
NewDays          5
Name: count, dtype: int64
```

### Proximity Network Output
```
   indices
0  [FamilyMart, Lawson]
1  [7-Eleven, NewDays, FamilyMart]
2  [7-Eleven]
...
```

## 🏗️ Project Structure

```
Geospatial_Patterns/
├── main.py                 # Main script with example usage
├── geospatial_analysis.py  # Core analysis class
├── example_configs.py      # Pre-configured examples
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT License
├── AI_ASSISTANT_PROMPT.md # AI assistant usage guide
├── .gitignore             # Git ignore rules
└── cache/                 # OSM data cache (gitignored)
```

## 🛠️ Technical Details

### Algorithms

- **Geocoding**: Uses OSMnx to convert location names to geographic boundaries
- **Spatial Queries**: Retrieves entities using OpenStreetMap Overpass API
- **Proximity Search**: Implements BallTree with Haversine metric for efficient nearest-neighbor search
- **Coordinate System**: Uses WGS84 (EPSG:4326) for geographic coordinates

### Walking Distance Calculation

The default walking radius of 168 meters represents approximately a 2-minute walk, assuming:
- Average walking speed: 1.4 m/s (5 km/h)
- Calculation: 1.4 m/s × 120 seconds = 168 meters

To customize: `walking_radius_meters = speed_m_per_s × time_seconds`

## 🤖 Working with AI Assistants

Need help with this project? Check out [AI_ASSISTANT_PROMPT.md](AI_ASSISTANT_PROMPT.md) for ready-to-use prompts that give AI assistants the context they need to help you effectively.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [OSMnx](https://osmnx.readthedocs.io/) - For OpenStreetMap data retrieval
- [GeoPandas](https://geopandas.org/) - For geospatial data manipulation
- [Scikit-learn](https://scikit-learn.org/) - For BallTree spatial indexing
- [OpenStreetMap](https://www.openstreetmap.org/) - For geographic data

## 📧 Contact

Project Link: [https://github.com/MarlinZH/Geospatial_Patterns](https://github.com/MarlinZH/Geospatial_Patterns)

## 🐛 Known Issues

- Entity extraction relies on `brand:en` tag availability in OSM data
- Large areas or dense urban regions may have slow query times
- Requires internet connection for OSM data retrieval

## 🔮 Future Enhancements

- [ ] Add interactive map visualizations with Folium
- [ ] Support for batch processing multiple areas
- [ ] Time-series analysis of entity changes
- [ ] Heat map generation for entity density
- [ ] CLI interface with argument parsing
- [ ] Web API for programmatic access
- [ ] Support for custom distance metrics
- [ ] Export to GeoJSON format

---

**Note**: This tool uses OpenStreetMap data. Please review the [OSM Copyright and License](https://www.openstreetmap.org/copyright) for data usage terms.
