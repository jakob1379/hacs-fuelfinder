"""Sensor to fetch fuel prices."""
import logging
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from fuelfinder import fetch_gas_prices

SCAN_INTERVAL = timedelta(minutes=5)
LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor."""
    async_add_entities([FuelPriceSensor()])

class FuelPriceSensor(Entity):
    """Representation of a Fuelfinder sensor."

    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._attributes = {}

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            data = fetch_gas_prices("https://www.fuelfinder.dk/listprices.php")
            self._state = data.to_dict()  # Example processing, adapt as needed
        except Exception as e:
            LOGGER.error("Error fetching fuel prices: %s", e)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Fuelfinder Fuel Prices"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
