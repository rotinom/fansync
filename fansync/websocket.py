
import json
import ssl

from websocket import WebSocketTimeoutException

from fansync import DeviceFactory
from fansync.exceptions import WebsocketAlreadyConnectedException, \
    WebsocketAuthException, TimedOutException
from fansync.facades import *
import websocket


class Websocket:
    API_URL = "wss://fanimation.apps.exosite.io/api:1/phone"

    def __init__(self, auth_token: SecretStr):
        self._id: int = 1  # creds.id
        self._token: SecretStr = auth_token
        self._websocket: Optional[websocket.WebSocket] = None

    def _get_id(self) -> int:
        """
        Method to get ID's for the communication protocol
        :return: ID for message
        """
        ret = self._id
        self._id += 1
        return ret

    def _send(self, request: Request):
        self._websocket.send(request.model_dump_json())

    def _recv(self) -> str:
        try:
            return self._websocket.recv()
        except WebSocketTimeoutException as e:
            print("timed out", flush=True)
            raise TimedOutException(e)

    def connect(self):
        if self._websocket:
            raise WebsocketAlreadyConnectedException()

        print(f"ws connect: {Websocket.API_URL}...", end="", flush=True)

        # websocket.enableTrace(True)
        self._websocket = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        self._websocket.timeout = 10
        self._websocket.connect(Websocket.API_URL)

        print("connected")

    def login(self):
        payload = LoginRequest(id=self._get_id(), data=LoginRequest.Data(token=self._token.get_secret_value()))
        print("Logging in websocket...", end="", flush=True)
        self._send(payload)

        try:
            resp = self._recv()
            print(resp)
            response = WsLoginResponse(**json.loads(resp))
        except WebSocketTimeoutException as e:
            print("timed out", flush=True)
            raise WebsocketAuthException(e)

        if response.status != "ok":
            print("failed", flush=True)
            print(f"Response: {response}")
            raise WebsocketAuthException("Failed to login websocket")

        print("done", flush=True)

    def close(self, code: int = 1000, msg: bytes = b"goodbye"):
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
        ret = ListDevicesResponse(**json.loads(self._recv()))
        print(ret)
        print(f"Received {len(ret.data)} devices")

        return ret

        # self._websocket.send(json.dumps(req.model_dump()))
        # ret = ListDevicesResponse(**json.loads(self._websocket.recv()))
        # print(f"Received: {ret}")


        #
        # for device in ret.data:
        #     d : Device = self.get_device(device)

    def set_device(self, device_id: str, data: dict[str, str]):
        request = \
            SetRequest(
                id=self._get_id(),
                device=device_id,
                data=data)

        self._send(request)

    def get_device(self, device: ListDevicesResponse.Device) -> GetDeviceResponse:
        # print(f"Querying device '{device.properties.displayName} ({device.device})'")

        request = GetDeviceRequest(
            id=self._get_id(),
            device=device.device)

        self._send(request)
        ret = GetDeviceResponse(**json.loads(self._recv()))
        # print(ret)

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

