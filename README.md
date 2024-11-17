
# Automated Security Testing Plugin (ASTP)

## Overview
This plugin automates tasks such as parameter tampering and token analysis to enhance web application security testing.

## Features
- **Parameter Tampering**: Test the integrity of HTTP request parameters.
- **Token Analysis**: Decode and validate JWT tokens for common vulnerabilities.

## Setup Instructions
1. Ensure you have Python 3.x installed.
2. Install dependencies with:
   ```
   pip install -r requirements.txt
   ```
3. Run the plugin:
   ```
   python src/main.py
   ```

## File Structure
- `src/`: Contains the source code.
- `config/`: Stores configuration files.
- `logs/`: Logs results of tests.
- `docs/`: Documentation and examples.

## Example Usage
1. Parameter tampering:
   - Configure `config/params_config.json`.
   - Run the script to test parameters against a target endpoint.
2. Token analysis:
   - Provide a JWT token in `config/token_config.json`.
   - Analyze for expiration, signature, and algorithm vulnerabilities.

## Contributing
Feel free to enhance the functionality by adding new modules or improving existing features.

## License
MIT License
