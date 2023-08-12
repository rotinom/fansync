from fansync.models import GetDeviceResponse


class DeviceFactory:

    def __init__(self, config_json_obj):
        self._config = config_json_obj
        # for k in config_json_obj.keys():
        #     print(k)

    def getDevice(self, device_response: GetDeviceResponse):
        pass