
import json

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
    API_URL = "wss://fanimation.apps.exosite.io"

    def __init__(self, creds: Credentials, device_factory: DeviceFactory):
        self._id: int = creds.id
        self._token: str = creds.token
        self._device_factory: DeviceFactory = device_factory
        self._devices = []
        self._websocket: ClientConnection = self._connect(Websocket.API_URL)

        # Perform login
        self._login(self._token)

    def _get_id(self):
        ret = self._id
        self._id += 1
        return ret

    def _handle_device_change_event(self, message):
        print(message)
        event = DeviceChangeEvent(**message)

        # Extract the encoded status
        self._status = event.data.changes.status

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

    @staticmethod
    def _connect(url: str) -> ClientConnection:

        # disable cert verification
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        endpoint = url + "/api:1/phone"

        print(f"Attempting to connect to: {url}...", end="")
        websocket = None
        for i in range(0, 3):
            try:
                websocket = ws_connect(endpoint, open_timeout=10, ssl_context=ssl_ctx)
                break
            except TimeoutError as e:
                print("\n\nTimed out trying to connect to: %s\n%s" % (endpoint, e))

        if websocket is None:
            raise Exception("Could not connect websocket to: %s" % (endpoint))

        print("done")
        return websocket

    def _login(self, token: str):
        # print(f"Logging in with token {token}")
        data = LoginRequest.Data(token=token)
        payload = LoginRequest(id=self._get_id(), data=data)

        print("Logging in websocket...", end="")
        self._websocket.send(payload.model_dump_json())
        response = LoginResponse(**json.loads(self._websocket.recv()))

        if response.status != "ok":
            raise Exception("Failed to login websocket")

        print("done")

    def run(self):
        # Perform initial enumeration of devices
        device_response = self.list_devices()

        for d in device_response.data:
            device = WebsocketDevice(self._device_factory, self._websocket, d)
            device.set_device_state(self.get_device(d))




    async def runnnn(self):

        # disable cert verification
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        uri = self.API_URL + "/api:1/phone"
        async with websockets.connect(uri,
                                      ssl=ssl_ctx,
                                      # This *seems* to make the connects more reliable...
                                      close_timeout=None) as websocket:
            payload = json.dumps({
                "id": self._get_id(),
                "request": "login",
                "data": {
                    "token": self._token
                }
            })
            print("Logging in websocket...")
            await websocket.send(payload)
            response = await websocket.recv()
            print(response)



            print("Provisioning token..")
            payload = json.dumps({
                "id": self._get_id(),
                "request": "provision_token",
                "data": {
                    "expires_in": 2592000
                }
            })
            await websocket.send(payload)
            response = await websocket.recv()
            print(response)

            # Perform initial enumeration of devices
            device_response = await self.list_devices(websocket)

            for d in device_response.data:
                getDevice = await self.get_device(websocket, d)



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
        req = ListDevicesRequest(
            id=self._get_id(),
            request="lst_device"
        )

        self._websocket.send(req.model_dump_json())
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

        req = GetDeviceRequest(
            id=self._get_id(),
            request="get",
            device=device.device)

        self._websocket.send(req.model_dump_json())
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

