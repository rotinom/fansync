from typing import Optional

import requests
import ssl
from websockets.sync.client import connect
import json
from collections.abc import Sequence
from pydantic import BaseModel, Field


class DeviceProperties(BaseModel):
    displayName: str
    deviceHasBeenConfigured: bool
    ignoreUpdateVersion: str


class Device(BaseModel):
    owner: str = None
    device: str = None
    role: str = None
    properties: DeviceProperties


class Request(BaseModel):
    id: int
    request: str
    data: Optional[dict[str, str]] = None


class GetDeviceRequest(Request):
    device: str


class Response(BaseModel):
    id: int
    status: str
    response: str


class User(BaseModel):
    role: str
    email: str


class GetDeviceEsh(BaseModel):
    brand: str
    esh_version: str
    class_: int = Field(alias="class")  # keyword in Python
    device_id: str
    model: str


class GetDeviceModule(BaseModel):
    firmware_version: str
    local_ip: str
    ssid: str
    mac_address: str


class GetDeviceProfile(BaseModel):
    module: GetDeviceModule
    esh: GetDeviceEsh

    class Config:
        exclude = ['cert']


class GetDeviceResponseData(BaseModel):
    users: list[User]
    status: dict[str, int]
    fields: list[str]
    profile: GetDeviceProfile
    # calendar - excluded
    device: str
    connected: int
    device_state: str

    # class Config:
    #     exclude = ['calendar']


class FanSync:

    def __init__(self):
        self._client = requests

        self._sessionId = None
        self._token = None
        self._id = 1
        self._websocket = None


    def login(self, email, password):
        r = self._client.post('https://fanimation.apps.exosite.io/api:1/session',
                              json={"email": email, "password": password})

        if r.status_code != 200:
            print("Failed to login")

        ret = r.json()
        self._sessionId = ret["id"]
        self._token = ret["token"]

    def _get_id(self):
        ret = self._id
        self._id += 1
        return ret

    def ws_connect(self):

        # disable cert verification
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        self._websocket = connect("wss://fanimation.apps.exosite.io:443/api:1/phone", ssl_context=ssl_ctx)

        self.ws_login()

    def ws_close(self):
        self._websocket.close()

    def ws_login(self):

        print("Logging in websocket...")
        data = json.dumps({
            "id": self._get_id(),
            "request": "login",
            "data": {
                "token": self._token
            }
        })
        self._websocket.send(data)
        message = self._websocket.recv()
        print(f"Received: {message}")


        print("Provisioning token..")
        data = json.dumps({
            "id": self._get_id(),
            "request": "provision_token",
            "data": {
                "expires_in": 2592000
            }
        })
        self._websocket.send(data)
        message = self._websocket.recv()
        print(f"Received: {message}")


    def ws_list_devices(self):

        print("Listing devices...")
        data = json.dumps({
            "id": self._get_id(),
            "request": "lst_device"
        })
        self._websocket.send(data)
        message = json.loads(self._websocket.recv())
        print(f"Received: {message}")

        ret = []
        for d in message["data"]:
            ret.append(Device(**d))

        return ret

    def ws_get_device(self, device_id):
        req = GetDeviceRequest(
            id=self._get_id(),
            request="get",
            device=device_id)

        self._websocket.send(json.dumps(req.model_dump()))

        message = json.loads(self._websocket.recv())
        print(f"Received: {message}")

        ret = []

        ret.append(GetDeviceResponseData(**message["data"]))

        print(ret)



    def fuzz(self, url, use_auth=False):

        headers = []
        if use_auth:
            headers = {"Authorization:",  "Bearer %s" % self._token}

        methods = [
            self._client.get,
            self._client.head,
            self._client.post,
            self._client.put,
            # self._client.delete,
            self._client.options,
            self._client.patch
        ]

        ignore_codes = set()
        ignore_codes.add(404)
        ignore_codes.add(415)

        for m in methods:

            r = m(url, headers=headers)
            if r.status_code in ignore_codes:
                continue

            print("%s %s - %s" % (m.__name__.upper(), url, r.status_code))
            try:
                if r.content.strip() != "":
                    pass
                    print(r.content)
                    # print(r.headers)
            except:
                # Swallow
                pass

