from websockets.client import ClientConnection

from fansync import DeviceFactory
from fansync.models import *

# # Not really a facade.  Trying this whole thing out right now
# class Device:
#
#     def __init__(self, device_factory: DeviceFactory, websocket: ClientConnection, device: ListDevicesResponse.Device):
#         self._ws = websocket
#         self._df = device_factory
#         self._listed_device: ListDevicesResponse.Device = device
#         self._device_state: Optional[GetDeviceResponse] = None
#
#     # Update with data from set_device
#     def set_device_state(self, device_state: GetDeviceResponse):
#         self._device = self._df.


class Light:

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


class Fan:
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

