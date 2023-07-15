

from fansync import FanSync


class Device:

    def __init__(self, fansync: FanSync, device_id: str):
        self._id = device_id


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

