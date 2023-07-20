
import requests
import json
from fansync.websocket import *


class FanSync:
    API_URL = "https://fanimation.apps.exosite.io"

    def __init__(self):
        self._client = requests
        self._token = None
        self._id = 1
        self._status = {}
        self._websocket = None

    def close(self):
        self._websocket.close()

    def open(self, email, password):
        options_headers = {
            "access-control-request-method": "POST",
            "origin": "http://localhost",
            "access-control-request-headers": "content-type"
        }

        o = self._client.options(self.API_URL + '/api:1/session',
                                 headers=options_headers)
        if o.status_code != 200:
            print("Failed to set login OPTIONS")

        r = self._client.post(self.API_URL + '/api:1/session',
                              json={"email": email, "password": password})

        if r.status_code != 200:
            print("Failed to login")

        ret = r.json()
        self._id = int(ret["id"])
        self._token = ret["token"]

        print(f"Got token of: {self._token}")

        self._websocket = Websocket(self._token, self._id, self._client)

        self._websocket.connect()

        # self._websocket.start()

        # for device in self._websocket.list_devices():
        #     pass



