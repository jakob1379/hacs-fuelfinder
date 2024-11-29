"""Config flow for Fuelfinder integration."""
from homeassistant import config_entries
from .const import DOMAIN

class FuelfinderConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fuelfinder."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLLING

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Fuelfinder", data=user_input)

        return self.async_show_form(step_id="user")
