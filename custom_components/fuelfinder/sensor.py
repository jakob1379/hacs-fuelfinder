"""Sensor to fetch fuel prices."""

import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION
from fuelfinder import fetch_gas_prices

SCAN_INTERVAL = timedelta(minutes=5)
LOGGER = logging.getLogger(__name__)

ATTRIBUTION = "Data provided by fuelfinder.dk"

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Fuelfinder sensor from a config entry."""
    async_add_entities([FuelPriceSensor()])


class FuelPriceSensor(SensorEntity):
    """Representation of a Fuelfinder sensor."""

    _attr_name = "Fuelfinder Fuel Prices"
    _attr_icon = "mdi:gas-station"

    def __init__(self):
        """Initialize the sensor."""
        self._attr_state = None
        self._attr_extra_state_attributes = {
            ATTR_ATTRIBUTION: ATTRIBUTION
        }

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            data = fetch_gas_prices("https://www.fuelfinder.dk/listprices.php")
            self._attr_state = data.to_dict()  # Example processing, adapt as needed
            # Add any other attributes you might want from the data
            self._attr_extra_state_attributes.update(data.describe()) # Example
        except Exception as e:
            LOGGER.error("Error fetching fuel prices: %s", e)
            self._attr_state = None

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return "fuelfinder_fuel_prices_sensor"

