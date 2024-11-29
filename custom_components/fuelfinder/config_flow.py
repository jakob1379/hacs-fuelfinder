"""Sensor to fetch fuel prices."""
import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from fuelfinder import fetch_gas_prices

SCAN_INTERVAL = timedelta(minutes=5)
LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor based on a config entry."""
    async_add_entities([FuelPriceSensor()])


class FuelPriceSensor(SensorEntity):
    """Representation of a Fuelfinder sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {}
        self._name = "Fuelfinder Fuel Prices"

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            # Assuming the function returns a dictionary
            data = await hass.async_add_executor_job(fetch_gas_prices, "https://www.fuelfinder.dk/listprices.php")
            if data:
                self._state = "Available"  # Set a relevant string to show the status
                # Setting the state attributes as the fetched data
                self._attributes = data  # This might be a nested dict structure
            else:
                self._state = "No data available"
        except Exception as e:
            LOGGER.error("Error fetching fuel prices: %s", e)
            self._state = "Error"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

