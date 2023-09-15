
from typing import Optional
from pydantic import BaseModel, Field, SecretStr, field_serializer
from typing import Union

from fansync.devices.light import field_mapping_


class InfoModel(BaseModel):
    class ModelValue(BaseModel):
        value: int
        text: str

    class Model(BaseModel):
        key: str
        # Either a LIST of value -> text  OR  a DICT of string -> int | str
        values: Union[dict[str, Union[int, str]], list['ModelValue']]

    class Component(BaseModel):
        type: str
        models: list['Model']
        title: str

    class ErrorFields(BaseModel):
        key: str
        values: list['ModelValue']

    class InformationModel(BaseModel):
        scheduleLayout: dict[str, list[str]]
        familyMembers: list[str]
        deviceId: str
        familyName: str
        components: dict[str, 'Component']
        errorFields: list['ErrorFields']

    timestamp: int
    size: int
    lastModified: int
    name: str
    informationModel: InformationModel


class HttpCredentials(BaseModel):
    email: SecretStr
    password: SecretStr


class Credentials(BaseModel):
    id: int
    token: SecretStr


class Request(BaseModel):
    id: int
    request: str


class SetRequest(Request):
    request: str = "set"
    device: str
    data: dict[str, str]


class Response(BaseModel):
    id: int
    status: str


class WsResponse(Response):
    response: str


class ProvisionTokenRequest(Request):
    class Data(BaseModel):
        expires_in: int = 2592000  # 30 days in seconds(?)

    request: str = "provision_token"
    data: Data


class ProvisionTokenResponse(WsResponse):
    class Data(BaseModel):
        token: str
        expires_in: int

    data: Data


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


class WsLoginResponse(WsResponse):
    pass


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
    request: str = "get"
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
