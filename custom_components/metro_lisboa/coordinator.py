import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import API_URL, DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class MetroLisboaCoordinator(DataUpdateCoordinator[dict]):
    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=SCAN_INTERVAL),
        )
        self._session = async_get_clientsession(hass)

    async def _async_update_data(self) -> dict:
        try:
            async with self._session.get(API_URL) as response:
                response.raise_for_status()
                # content_type=None because the API returns text/html despite sending JSON
                data = await response.json(content_type=None)
        except Exception as err:
            raise UpdateFailed(f"Error fetching Metro Lisboa status: {err}") from err

        if data.get("codigo") != "200":
            raise UpdateFailed(f"API returned error: {data.get('codigo')}")

        return data["resposta"]
