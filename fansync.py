from datetime import datetime
from typing import Optional

import requests
import ssl
from websockets.sync.client import connect
import json
from models import *
from threading import *



class FanSync:

    def __init__(self):
        self._client = requests

        self._sessionId = None
        self._token = None
        self._id = 1
        self._websocket = None
        self._ws_recv_thread = Thread(target=self._ws_recv)

        self._status = {}

        # Mapping of event type -> member functions to handle the events
        self._eventDispatchDict = {
            'device_change': self._handleDeviceChangeEvent
        }


    def _ws_recv(self):
        while True:
            message = json.loads(self._websocket.recv())

            if "event" in message:
                key = message["event"]
                print("Using event key of: %s" % key)
                # try:
                self._eventDispatchDict[key](message)

                # except as e:
                #     print("Failed to handle message: %s" % message)

            else:
                print(message)

    def _handleDeviceChangeEvent(self, message):
        print(message)
        event = DeviceChangeEvent(**message)

        # Extract the encoded status
        self._status = event.data.changes.status


    def login(self, email, password):

        options_headers = {
            "access-control-request-method": "POST",
            "origin": "http://localhost",
            "access-control-request-headers": "content-type"
        }

        o = self._client.options('https://fanimation.apps.exosite.io/api:1/session',
                                 headers=options_headers)
        if o.status_code != 200:
            print("Failed to set login OPTIONS")


        r = self._client.post('https://fanimation.apps.exosite.io/api:1/session',
                              json={"email": email, "password": password})

        if r.status_code != 200:
            print("Failed to login")

        ret = r.json()
        self._id = int(ret["id"])
        self._token = ret["token"]

        print(f"Got token of: {self._token}")

    def _get_id(self):
        ret = self._id
        self._id += 1
        return ret

    def ws_connect(self):

        # disable cert verification
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        host = "wss://fanimation.apps.exosite.io:443/api:1/phone"
        print(f"Connecting to host: {host}")
        self._websocket = connect(host, ssl_context=ssl_ctx)

        self.ws_login()

        print("Starting receive thread")
        self._ws_recv_thread.start()

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
        # print(f"Received: {message}")


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
        # print(f"Received: {message}")


    def ws_list_devices(self):

        # print("Listing devices...")
        req = ListDevicesRequest(
            id=self._get_id(),
            request="lst_device"
        )

        self._websocket.send(json.dumps(req.model_dump()))
        # ret = ListDevicesResponse(**json.loads(self._websocket.recv()))
        # print(f"Received: {ret}")
        # return ret

    def ws_get_device(self, device: ListDevicesResponse.Device):
        # print(f"Querying device '{device.properties.displayName} ({device.device})'")

        req = GetDeviceRequest(
            id=self._get_id(),
            request="get",
            device=device.device)

        self._websocket.send(json.dumps(req.model_dump()))

#         raw = json.loads(self._websocket.recv())
#         print(raw)
#
#         ret = GetDeviceResponse(**raw)
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

