from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, LINE_MSG_KEYS, LINES
from .coordinator import MetroLisboaCoordinator

DEVICE_INFO = DeviceInfo(
    identifiers={(DOMAIN, "metro_lisboa")},
    name="Metro de Lisboa",
    manufacturer="Metro de Lisboa",
    model="Line Status",
    configuration_url="https://www.metrolisboa.pt",
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: MetroLisboaCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        MetroLineBinarySensor(coordinator, line_key, line_name)
        for line_key, line_name in LINES.items()
    )


class MetroLineBinarySensor(CoordinatorEntity[MetroLisboaCoordinator], BinarySensorEntity):
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.PROBLEM

    def __init__(
        self,
        coordinator: MetroLisboaCoordinator,
        line_key: str,
        line_name: str,
    ) -> None:
        super().__init__(coordinator)
        self._line_key = line_key
        self._msg_key = LINE_MSG_KEYS[line_key]
        self._attr_name = line_name
        self._attr_unique_id = f"metro_lisboa_{line_key}"
        self._attr_device_info = DEVICE_INFO

    @property
    def is_on(self) -> bool | None:
        if self.coordinator.data is None:
            return None
        raw = self.coordinator.data.get(self._line_key, "").strip()
        tipo_msg = self.coordinator.data.get(self._msg_key, "0")
        # is_on=True means problem/disruption
        return not (raw.lower() == "ok" and tipo_msg == "0")

    @property
    def extra_state_attributes(self) -> dict:
        if self.coordinator.data is None:
            return {}
        return {
            "status": self.coordinator.data.get(self._line_key, "").strip(),
            "message_type": self.coordinator.data.get(self._msg_key, "0"),
        }
