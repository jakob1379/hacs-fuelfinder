<h1 align="center">Fuelfinder for Home Assistant</h1>

<p align="center">
  Danish fuel and EV charging prices from <a href="https://www.fuelfinder.dk">fuelfinder.dk</a>, as Home Assistant sensors.
</p>

<p align="center">
  <a href="https://hacs.xyz"><img src="https://img.shields.io/badge/HACS-Custom-41BDF5" alt="HACS custom repository"></a>
  <a href="https://github.com/jakob1379/hacs-fuelfinder/actions/workflows/validate.yml"><img src="https://github.com/jakob1379/hacs-fuelfinder/actions/workflows/validate.yml/badge.svg" alt="Validate workflow status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>

<p align="center">
  <img src=".github/assets/fuelfinder-flow.svg" width="100%" alt="Diagram: the fuelfinder.dk price list has one row per fuel company and one column per fuel type. For each fuel type the lowest listed price is picked and becomes the state of a Home Assistant sensor such as Fuelfinder - Blyfri 95 (E10). Prices shown are illustrative.">
</p>

Fuelfinder is a custom integration that reads the public price list at
[fuelfinder.dk/listprices.php](https://www.fuelfinder.dk/listprices.php) and
creates one sensor per fuel type. Each sensor's state is the lowest price any
company lists for that fuel; the full list of company prices is kept in the
sensor's attributes.

## What you get

- **One sensor per fuel type**, named `Fuelfinder - <fuel type>`.
- **Cheapest price as the state**, so it can drive automations and dashboards directly.
- **Every company's price as attributes**, plus `fuel_type` and an attribution to fuelfinder.dk.
- **Gentle on the source**: sensors poll once an hour, and the underlying
  [`fuelfinder`](https://pypi.org/project/fuelfinder/) library caches responses for 5 minutes.

Sensors are created for the fuel types below that are present in the price list
when the integration is set up:

| Petrol | Diesel and HVO | EV charging |
| --- | --- | --- |
| Blyfri 92 | Diesel (B7) | EL normal |
| Blyfri 95 (E10) | Diesel + | EL hurtig |
| Blyfri 95+ (E10) | HVO (XTL) | EL lyn |
| Blyfri + (E5) | | |

## Installation

Requires Home Assistant 2024.11.3 or newer.

### HACS

1. Open **HACS** in Home Assistant.
2. Open the **three-dot menu** in the top right corner and select **Custom repositories**.
3. Add `https://github.com/jakob1379/hacs-fuelfinder` and select **Integration** as the type.
4. Find **Fuelfinder** in HACS and install it.
5. Restart Home Assistant.

### Manual

1. Copy the `custom_components/fuelfinder` directory into your Home Assistant `custom_components` directory.
2. Restart Home Assistant.

## Configuration

1. Go to **Settings** > **Devices & services**.
2. Select **Add integration** and choose **Fuelfinder**.
3. Submit the form. There is nothing to fill in; the sensors appear once the first prices are fetched.

## License

MIT. See [LICENSE](LICENSE) for details. Price data is provided by
[fuelfinder.dk](https://www.fuelfinder.dk).
