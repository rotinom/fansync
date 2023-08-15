from fansync import GetDeviceResponse, Websocket


class Device:
    """
    Not super happy w/ this arrangement. We'll see if it sticks.
    Basically this would be a friend class of Websocket? Need to get this
    working first and see how it feels to mess with it at the top layer
    """
    def __init__(self,

                 websocket: Websocket,
                 display_name: str,
                 device: GetDeviceResponse):
        self.websocket: Websocket = websocket
        self.display_name: str = display_name
        self.device: str = device

        self.lights: list[Light] = []
        self.fans: list[Fan] = []


class Light:

    def __init__(self, device: Device):
        self._device = device

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
    def __init__(self, device: Device):
        self._device = device

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