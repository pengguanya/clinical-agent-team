# Contributing to Workforce Crews

Thank you for your interest in contributing to the Workforce Crews project! This document provides guidelines and instructions for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine
3. **Set up the development environment** following the instructions in the [Quick Start Guide](quickstart.md)

## Development Workflow

1. **Create a branch** for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure they follow the project's coding standards

3. **Test your changes** thoroughly
   ```bash
   # Run tests if available
   pytest
   ```

4. **Commit your changes** with clear and descriptive commit messages
   ```bash
   git commit -m "Feature: Add description of your changes"
   ```

5. **Push your changes** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a pull request** from your fork to the main repository

## Types of Contributions

### Adding New Crews

To add a new crew:

1. Create a new directory in `src/crews/your_crew_name/`
2. Create a `config` directory with YAML files for agent and task definitions
3. Implement the crew logic in a main Python file
4. Add documentation in the `docs` directory
5. Update the README with information about your crew

### Enhancing Existing Crews

To enhance an existing crew:

1. Identify the crew you want to improve
2. Make your changes, ensuring backward compatibility
3. Test your changes thoroughly
4. Document the enhancements

### Adding New Tools

To add new tools for agents:

1. Implement the tool in the appropriate directory
2. Ensure the tool follows the established patterns
3. Add documentation for the tool
4. Update the README with information about your tool

## Code Standards

- Follow PEP 8 for Python code
- Use type annotations where possible
- Maintain test coverage for new features
- Document code using docstrings

## Documentation

When contributing, please update the documentation to reflect your changes:

- Update relevant markdown files in the `docs` directory
- Add examples for new features
- Update the README if necessary

## Pull Request Process

1. Ensure your code follows the project's standards
2. Update the documentation to reflect your changes
3. Add tests for new features
4. Make sure all tests pass
5. Submit your pull request with a clear description of the changes

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We follow a code of conduct that promotes a positive and inclusive environment for everyone.

## Questions?

If you have any questions about contributing, please [open an issue](https://github.com/yourusername/workforce-crews/issues/new) or contact the project maintainers.

Thank you for your contributions! 