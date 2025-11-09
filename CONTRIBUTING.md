# Contributing to Geospatial Patterns

Thank you for your interest in contributing to Geospatial Patterns! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (OS, Python version, package versions)
- Any relevant code snippets or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear description of the enhancement
- Use cases and examples
- Why this enhancement would be useful
- Any potential implementation ideas

### Pull Requests

1. **Fork the repository** and create your branch from `master`:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes**:
   - Write clear, documented code
   - Follow the existing code style
   - Add docstrings to functions and classes
   - Update documentation as needed

3. **Test your changes**:
   - Ensure your code works as expected
   - Test with different areas and entity types
   - Check for any breaking changes

4. **Commit your changes**:
   ```bash
   git commit -m "feat: Add amazing feature"
   ```
   
   Use conventional commit messages:
   - `feat:` New features
   - `fix:` Bug fixes
   - `docs:` Documentation changes
   - `refactor:` Code refactoring
   - `test:` Adding tests
   - `chore:` Maintenance tasks

5. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**:
   - Provide a clear description of changes
   - Reference any related issues
   - Explain the motivation behind changes

## 💻 Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Geospatial_Patterns.git
   cd Geospatial_Patterns
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a new branch:
   ```bash
   git checkout -b your-feature-branch
   ```

## 📝 Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add type hints where appropriate
- Write docstrings for all public functions and classes
- Keep functions focused and single-purpose
- Maximum line length: 100 characters

### Example:

```python
def calculate_distance(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float
) -> float:
    """
    Calculate the haversine distance between two points.
    
    Args:
        lat1: Latitude of first point
        lon1: Longitude of first point
        lat2: Latitude of second point
        lon2: Longitude of second point
        
    Returns:
        Distance in meters
    """
    # Implementation here
    pass
```

## 🧪 Testing

Before submitting a PR:
- Test your changes with multiple areas and entity types
- Verify that existing functionality still works
- Check for edge cases (empty results, large datasets, etc.)

## 📚 Documentation

Update documentation when:
- Adding new features
- Changing public APIs
- Modifying configuration options
- Adding new examples

## 🎯 Priority Areas for Contribution

We're particularly interested in contributions for:

1. **Interactive Visualizations**: Add folium maps or plotly charts
2. **Additional Export Formats**: GeoJSON, KML, or Shapefile support
3. **Performance Optimization**: For large datasets
4. **CLI Interface**: Command-line argument parsing
5. **Unit Tests**: Comprehensive test coverage
6. **Additional Analysis Features**: Heat maps, cluster analysis, etc.
7. **Documentation**: More examples, tutorials, or use cases

## ❓ Questions?

If you have questions about contributing:
- Open an issue with the `question` label
- Check existing issues for similar questions
- Review the README for basic usage information

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in the project README. Thank you for helping improve Geospatial Patterns!
