
import json
from typing import TypeVar

from websockets.typing import Data

from fansync import DeviceFactory
from fansync.models import *
from threading import *
import ssl
from websockets.sync.client import connect as ws_connect, ClientConnection
import websockets
import requests
import asyncio
from fansync.facades import *
import models

T = TypeVar('T')                  # Declare type variable "T"


# TODO Use asyncio for websockets


class WebsocketAuthException(Exception):
    pass


class WebsocketNotConnectedException(Exception):
    pass


class WebsocketAlreadyConnectedException(Exception):
    pass


# Not really a facade.  Trying this whole thing out right now
class WebsocketDevice:

    def __init__(self, device_factory: DeviceFactory, websocket: ClientConnection, device: ListDevicesResponse.Device):
        self._ws = websocket
        self._df = device_factory
        self._listed_device: ListDevicesResponse.Device = device
        self._device_state: Optional[GetDeviceResponse] = None

    # Update with data from set_device
    def set_device_state(self, device_state: GetDeviceResponse):
        self._device = self._df.getDevice(device_state)

class WebsocketRequest:
    def __init__(self, websocket, headers, request: Request):
        pass


class Websocket:
    API_URL = "wss://fanimation.apps.exosite.io/api:1/phone"

    def __init__(self, auth_token: str):
        self._id: int = 1  # creds.id
        self._token: str = auth_token
        self._websocket: Optional[ClientConnection] = None


        # self._device_factory: DeviceFactory = device_factory
        # self._devices = []
        # self._websocket: ClientConnection = self._connect(Websocket.API_URL)
        #
        # # Perform login
        # try:
        #     self._login(self._token)
        #     self._provision_token()
        # except WebsocketAuthException as e:
        #     self.close(4001, "Websocket open failed.")
        #     raise e

    # Method to get ID's for the communication protocol
    def _get_id(self):
        ret = self._id
        self._id += 1
        return str(ret)

    def _send(self, request: Request):
        if not self._websocket:
            raise WebsocketNotConnectedException()

        data = request.model_dump_json()
        print(f"ws send {data}")
        self._websocket.send(data)

    # TODO: When this is working, try making this generic
    # def _recv(self, return_type: T, timeout: float = 5) -> T:
    def _recv(self,  timeout: float = 5.0) -> Data:

        if not self._websocket:
            raise WebsocketNotConnectedException()

        print(f"ws recv...", end="", flush=True)

        try:
            return self._websocket.recv(timeout)
        except TimeoutError as e:
            print("timed out", flush=True)
            raise e

    def connect(self):
        if self._websocket:
            raise WebsocketAlreadyConnectedException()

        # disable cert verification
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        print(f"ws connect: {Websocket.API_URL}...", end="", flush=True)
        try:
            user_agent = "Mozilla/5.0 (Linux; Android 9; ONEPLUS A3003 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36"
            headers = {
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "Origin": "http://localhost",
                "Accept-Language": "en-US,en;q=0.9",
            }
            self._websocket = \
                ws_connect(Websocket.API_URL,
                           user_agent_header=user_agent,
                           additional_headers=headers,
                           open_timeout=10,
                           ssl_context=ssl_ctx)

        except TimeoutError as e:
            print("timed out", flush=True)
            raise e

    def close(self, code: int = 1000, msg: str = "goodbye"):
        print(f"Closing websocket '{msg}({code})'")
        self._websocket.close(code, msg)
        self._websocket = None

    # TODO Not well tested
    def provision_token(self):
        payload = ProvisionTokenRequest(id=self._get_id(), data=ProvisionTokenRequest.Data())
        self._send(payload)
        try:
            response: LoginResponse = LoginResponse(**json.loads(self._recv()))
            # TODO do something w/ response
        except TimeoutError as e:
            raise WebsocketAuthException(e)

    # def _handle_device_change_event(self, message):
    #     print(message)
    #     event = DeviceChangeEvent(**message)
    #
    #     # Extract the encoded status
    #     self._status = event.data.changes.status

    # def _recv(self):
    #     while self._keep_running:
    #         message = json.loads(self._websocket.recv())
    #
    #         if "event" in message:
    #             key = message["event"]
    #             print("Using event key of: %s" % key)
    #             # try:
    #             self._eventDispatchDict[key](message)
    #
    #             # except as e:
    #             #     print("Failed to handle message: %s" % message)
    #
    #         else:
    #             print(message)



    def login(self):
        payload = LoginRequest(id=self._get_id(), data=LoginRequest.Data(token=self._token))

        print("Logging in websocket...", end="", flush=True)

        self._send(payload)
        try:
            response = LoginResponse(**json.loads(self._recv(timeout=5)))
        except TimeoutError as e:
            print("timed out", flush=True)
            raise WebsocketAuthException()

        if response.status != "ok":
            print("failed", flush=True)
            print(f"Response: {response}")
            raise Exception("Failed to login websocket")

        print("done", flush=True)

    # def run(self):
    #     # Perform initial enumeration of devices
    #     device_response = self.list_devices()
    #
    #     for d in device_response.data:
    #         device = WebsocketDevice(self._device_factory, self._websocket, d)
    #         device.set_device_state(self.get_device(d))




    # async def runnnn(self):
    #
    #     # disable cert verification
    #     ssl_ctx = ssl.create_default_context()
    #     ssl_ctx.check_hostname = False
    #     ssl_ctx.verify_mode = ssl.CERT_NONE
    #
    #     uri = self.API_URL + "/api:1/phone"
    #     async with websockets.connect(uri,
    #                                   ssl=ssl_ctx,
    #                                   # This *seems* to make the connects more reliable...
    #                                   close_timeout=None) as websocket:
    #         payload = json.dumps({
    #             "id": self._get_id(),
    #             "request": "login",
    #             "data": {
    #                 "token": self._token
    #             }
    #         })
    #         print("Logging in websocket...")
    #         await websocket.send(payload)
    #         response = await websocket.recv()
    #         print(response)
    #
    #
    #
    #         print("Provisioning token..")
    #         payload = json.dumps({
    #             "id": self._get_id(),
    #             "request": "provision_token",
    #             "data": {
    #                 "expires_in": 2592000
    #             }
    #         })
    #         await websocket.send(payload)
    #         response = await websocket.recv()
    #         print(response)
    #
    #         # Perform initial enumeration of devices
    #         device_response = await self.list_devices(websocket)
    #
    #         for d in device_response.data:
    #             getDevice = await self.get_device(websocket, d)



        #
        # for i in range(0, 3):
        #     try:
        #         self._websocket = ws_connect(endpoint, open_timeout=10, ssl_context=ssl_ctx)
        #         break
        #     except TimeoutError as e:
        #         print("Timed out trying to connect to: %s\n%s" % (endpoint, e))
        #
        # if self._websocket is None:
        #     raise Exception("Could not connect websocket to: %s" % (endpoint))
        #
        # self._start_recv_thread()
        #
        # self._login()
        # self._provision_token()

    #
    # def _start_recv_thread(self):
    #     print("Starting receive thread")
    #     self._ws_recv_thread.start()



    #
    # def close(self):
    #     # TODO kill any running threads
    #
    #     self._websocket.close()
    #
    # def _login(self):
    #
    #     data = json.dumps({
    #         "id": self._get_id(),
    #         "request": "login",
    #         "data": {
    #             "token": self._token
    #         }
    #     })
    #     print("Logging in websocket...")
    #     self._websocket.send(data)
    #
    #     #
    #     # message: str = None
    #     # for i in range(0, 5):
    #     #
    #     #
    #     #
    #     #     try:
    #     #         print("Waiting for login response...")
    #     #         message = self._websocket.recv(timeout=10)
    #     #         print(message)
    #     #         break
    #     #
    #     #     except TimeoutError as e:
    #     #         print("Timed out waiting for websocket login response")
    #     #
    #     # if message is None:
    #     #     raise TimeoutError("Timed out waiting for websocket login response")



    # def _provision_token(self):
    #     print("Provisioning token..")
    #     data = json.dumps({
    #         "id": self._get_id(),
    #         "request": "provision_token",
    #         "data": {
    #             "expires_in": 2592000
    #         }
    #     })
    #     self._websocket.send(data)
    #     # message = self._websocket.recv()
    #     # print(f"Received: {message}")

    def list_devices(self) -> ListDevicesResponse:

        print("Listing devices...")
        request = ListDevicesRequest(
            id=self._get_id(),
            request="lst_device"
        )

        self._send(request)
        ret = ListDevicesResponse(**json.loads(self._websocket.recv()))
        print(ret)
        print(f"Received {len(ret.data)} devices")

        return ret

        # self._websocket.send(json.dumps(req.model_dump()))
        # ret = ListDevicesResponse(**json.loads(self._websocket.recv()))
        # print(f"Received: {ret}")


        #
        # for device in ret.data:
        #     d : Device = self.get_device(device)



    def get_device(self, device: ListDevicesResponse.Device) -> GetDeviceResponse:
        # print(f"Querying device '{device.properties.displayName} ({device.device})'")

        request = GetDeviceRequest(
            id=self._get_id(),
            request="get",
            device=device.device)

        self._send(request)
        ret = GetDeviceResponse(**json.loads(self._websocket.recv()))
        print(ret)

        return ret

        # raw = json.loads(self._websocket.recv())
        # print(raw)
        #
        # ret = GetDeviceResponse(**raw)
#
#         fan_power = "On" if ret.data.get_fan_power() else "Off"
#         lgt_power = "On" if ret.data.get_light_power() else "Off"
#         home_away = "On" if ret.data.get_home_away() else "Off"
#
#         print(f""" \
# {datetime.now()}
#     {ret.data.profile.esh.brand} {ret.data.profile.esh.model}
#         Light: {lgt_power:3} ({ret.data.get_light_percent()}%)
#         Fan:   {fan_power:3} ({ret.data.get_fan_percent()}%)
#             Breeze Mode: {ret.data.get_fan_mode()}
#             Fan Direction: {ret.data.get_fan_direction()}
#         Home Away: {ret.data.get_home_away()}
#
#         Unknown:
#             H05: {ret.data.status['H05']}
#             H0E: {ret.data.status['H0E']}
# """)



    # def fuzz(self, url, use_auth=False):
    #
    #     headers = []
    #     if use_auth:
    #         headers = {"Authorization:",  "Bearer %s" % self._token}
    #
    #     methods = [
    #         self._client.get,
    #         self._client.head,
    #         self._client.post,
    #         self._client.put,
    #         # self._client.delete,
    #         self._client.options,
    #         self._client.patch
    #     ]
    #
    #     ignore_codes = set()
    #     ignore_codes.add(404)
    #     ignore_codes.add(415)
    #
    #     for m in methods:
    #
    #         r = m(url, headers=headers)
    #         if r.status_code in ignore_codes:
    #             continue
    #
    #         print("%s %s - %s" % (m.__name__.upper(), url, r.status_code))
    #         try:
    #             if r.content.strip() != "":
    #                 pass
    #                 print(r.content)
    #                 # print(r.headers)
    #         except:
    #             # Swallow
    #             pass

