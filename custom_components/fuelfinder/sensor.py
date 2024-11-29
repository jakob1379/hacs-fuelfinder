"""Sensors to fetch fuel prices."""
import logging
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from fuelfinder import fetch_gas_prices

SCAN_INTERVAL = timedelta(minutes=5)
LOGGER = logging.getLogger(__name__)

# Static fuel types we expect to always be present
EXPECTED_FUEL_TYPES = [
    "Blyfri 92",
    "Blyfri 95 (E10)",
    "Blyfri 95+ (E10)",
    "Blyfri + (E5)",
    "Diesel (B7)",
    "Diesel +",
    "HVO (XTL)",
    "EL normal",
    "EL hurtig",
    "EL lyn",
]

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the fuel price sensors."""
    try:
        # Fetch initial data to determine which sensors are available
        initial_data = fetch_gas_prices("https://www.fuelfinder.dk/listprices.php")
        if initial_data is None:
            LOGGER.error("Failed to retrieve initial data for fuel prices.")
            return

        entities = []
        for fuel_type in EXPECTED_FUEL_TYPES:
            if fuel_type in initial_data:
                entities.append(FuelPriceSensor(fuel_type, initial_data[fuel_type]))

        async_add_entities(entities, update_before_add=True)
    except Exception as e:
        LOGGER.error("Error during initial sensor setup: %s", e)

class FuelPriceSensor(Entity):
    """Representation of a Fuelfinder sensor for a specific fuel type."""

    def __init__(self, fuel_type, initial_data):
        """Initialize the sensor for a specific fuel type."""
        self._fuel_type = fuel_type
        self._state = None
        self._attributes = {
            "fuel_type": fuel_type,
            "attribution": "Data provided by fuelfinder.dk"
        }
        self.update_data(initial_data)

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            data = fetch_gas_prices("https://www.fuelfinder.dk/listprices.php")
            if data is not None and self._fuel_type in data:
                self.update_data(data[self._fuel_type])
            else:
                LOGGER.warning(f"No data found for fuel type '{self._fuel_type}'")
                self._state = "No data"
        except Exception as e:
            LOGGER.error("Error fetching fuel prices: %s", e)
            self._state = "unavailable"

    def update_data(self, fuel_data):
        """Update sensor state and attributes with fetched fuel data."""
        self._state = max(
            (price for price in fuel_data.values() if price is not None), default=None
        )
        self._attributes.update(fuel_data)

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Fuelfinder - {self._fuel_type}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

