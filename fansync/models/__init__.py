
from typing import Optional
from pydantic import BaseModel, Field, SecretStr, field_serializer
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


class HttpCredentials(BaseModel):
    email: SecretStr
    password: SecretStr


class Credentials(BaseModel):
    id: int
    token: SecretStr


class Request(BaseModel):
    id: int
    request: str


class Response(BaseModel):
    id: int
    status: str
    # response: str


class ProvisionTokenRequest(Request):
    class Data(BaseModel):
        expires_in: int = 2592000  # 30 days in seconds(?)

    request: str = "provision_token"


class LoginRequest(Request):
    class Data(BaseModel):
        token: SecretStr

        @field_serializer('token', when_used='json')
        def dump_secret(self, v):
            return v.get_secret_value()

    request: str = "login"
    data: Data


# This is weird. It's a special "Response" not related to the "Response" hierarchy
class LoginResponse(BaseModel):
    id: int
    token: SecretStr



class ListDevicesRequest(Request):
    pass


class ListDevicesResponse(Response):
    class Properties(BaseModel):
        displayName: str
        deviceHasBeenConfigured: bool
        ignoreUpdateVersion: str

    class Device(BaseModel):
        owner: str = None
        device: str = None
        role: str = None
        properties: 'Properties'

    data: list[Device]


class GetDeviceRequest(Request):
    device: str


class User(BaseModel):
    role: str
    email: str


class GetDeviceResponse(Response):

    class Module(BaseModel):
        firmware_version: str
        local_ip: str
        ssid: str
        mac_address: str

    class Esh(BaseModel):
        brand: str
        esh_version: str
        class_: int = Field(alias="class")  # keyword in Python
        device_id: str
        model: str

    class Data(BaseModel):

        class Profile(BaseModel):
            module: 'GetDeviceResponse.Module'  # forward reference
            esh: 'GetDeviceResponse.Esh'        # forward reference

            class Config:
                exclude = ['cert']

        users: list[User]
        status: dict[str, int]
        fields: list[str]
        profile: Profile
        # calendar - excluded
        device: str
        connected: int
        device_state: str

        def get_fan_percent(self):
            return self.status[field_mapping_['FAN_PERCENT']]

        def get_fan_power(self):
            return self.status[field_mapping_['FAN_POWER']] == 1

        def get_fan_mode(self):
            return fan_mode_[self.status[field_mapping_['FAN_MODE']]]

        def get_fan_direction(self):
            return fan_direction_[self.status[field_mapping_['FAN_DIRECTION']]]

        def get_light_percent(self):
            return self.status[field_mapping_['LIGHT_PERCENT']]

        def get_light_power(self):
            return self.status[field_mapping_['LIGHT_POWER']]

        def get_home_away(self):
            return self.status[field_mapping_['HOME_AWAY']] == 1

        # class Config:
        #     exclude = ['calendar']

    data: Data


# Best guess; only have one event type now
class Event(BaseModel):
    event: str


# Best guess; This is the only concrete event observed
class DeviceChangeEvent(Event):
    class Data(BaseModel):
        class Changes(BaseModel):
            status: dict[str, int]

        changes: 'Changes'
        device: str

    data: 'Data'
