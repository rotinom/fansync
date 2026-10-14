from typing import Optional

from bidict import *

# This is dynamically driven from values that come from
# GET /api:1/info-model
field_mapping_ = bidict({
    'FAN_POWER': 'H00',
    'FAN_MODE': 'H01',
    'FAN_PERCENT': 'H02',
    'FAN_DIRECTION': 'H06',
    'LIGHT_POWER': 'H0B',
    'LIGHT_PERCENT': 'H0C',
    'HOME_AWAY': 'H0D',
    'UNKNOWN1': 'H05',  # "TIMER" OR "FAN_LEARN_LOAD"
    'ERROR_CODE': 'H0E'  # OBSERVED VALUE '262'
})


fan_mode_ = bidict({
    0: "Normal",
    1: "Fresh Air"
})

fan_direction_ = bidict({
    0: "Forward",
    1: "Reverse"
})


class Light:

    def __init__(self, output_callback, power_key: str, percent_key: str):
        self._output_callback = output_callback
        self._power_key: str = power_key
        self._power_value: Optional[int] = None
        self._percent_key: str = percent_key
        self._percent_value: Optional[int] = None

    def set_status(self, status: dict[str, int]):
        if self._power_key in status:
            self._power_value = status[self._power_key]

        if self._percent_key in status:
            self._percent_value = status[self._percent_key]
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_percent(self):
        pass

    def get_percent(self):
        pass

    def is_on(self):
        pass





