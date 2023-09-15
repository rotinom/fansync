import json
import re
from typing import Optional

from fansync.devices.device import Device
from fansync.models import InfoModel, GetDeviceResponse

from pprint import pprint


"""
Fan/Light parameters specified in the information model 
FAN_DIRECTION
FAN_HOME_SHIELD
FAN_LEARN_LOAD
FAN_LIGHT
FAN_LIGHT_CCT
FAN_MODE
FAN_POWER
FAN_POWER_AND_SPEED
LIGHT_HOME_SHIELD
LIGHT_POWER
LIGHT_POWER_AND_DIMMER
LIGHT_TURN_OFF_TIMER
LIGHT_TURN_ON_TIMER
"""



class DeviceFactory:
    def __init__(self, info_model: dict[str, dict]):
        # self._info_model: dict[str, dict] = info_model
        self._regex_to_model: list[(str, InfoModel)] = []

        # Parse all the items
        for key, value in info_model.items():
            info_model: InfoModel = InfoModel(**value)

            # Create a list of regex's to InfoModel's so we can reference the
            # InfoModel when a regex matches
            for family_member in info_model.informationModel.familyMembers:
                regex = re.compile(family_member)
                self._regex_to_model.append((regex, info_model))

            # I don't remember why I did this...
            # for c in info_model.informationModel.components.keys():
            #     if not c:
            #         print("not present")



    def get_device(self, display_name: str, device_response: GetDeviceResponse) -> Optional[Device]:

        # Loop through all the downloaded candidates, and try to find a regex that matches
        # the esh model that we have
        found_model: Optional[InfoModel] = None
        for regex, info_model in self._regex_to_model:
            if regex.match(device_response.data.profile.esh.model):
                print(f"Found a model!")
                print(info_model.model_dump_json(indent=2))
                found_model: InfoModel = info_model
                break

        if not found_model:
            return None

        # Cool, so we have an InfoModel that describes this device.  Let's now make a device
        # based on the parameters that are in the InfoModel
        d = Device(display_name, device_response.data.profile.esh.device_id)

        # The device has N keys associated with it.  Those keys are enumerated in the InfoModel
        # that we have discovered.  So let's match those.
        for k in device_response.data.fields:
            for ck in found_model.informationModel.components:
                cv: InfoModel.Component = found_model.informationModel.components[ck]
                if cv.models[0].key == k:
                    print(f"{k} - {ck}")



        # d.fans.append(Fan())




