# Fuelfinder for Home Assistant

Fuelfinder is a custom Home Assistant component that provides current fuel prices from [fuelfinder.dk](https://www.fuelfinder.dk). It integrates with HACS (Home Assistant Community Store) for easy installation.

## Features
- **Real-time Fuel Prices**: Get up-to-date fuel prices.
- **Rate Limiting**: Requests are cached for 5 minutes to prevent excessive server requests.
- **Easy Integration with HACS**.

## Installation

### HACS Installation
1. Go to **HACS** in Home Assistant.
2. Click on **Integrations**.
3. Click on the **three dots** in the top right corner and select **Custom repositories**.
4. Add `https://github.com/yourusername/hacs-fuelfinder` and select **Integration** as the category.
5. Find **Fuelfinder** in HACS and install it.

### Manual Installation
1. Copy the `custom_components/fuelfinder` directory to your Home Assistant's `custom_components` directory.
2. Restart Home Assistant.

### Configuration
1. Go to **Configuration** > **Integrations**.
2. Add **Fuelfinder**.
3. Set up the options including the data source URL.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

