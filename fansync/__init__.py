
import os
from json import JSONDecodeError

import requests

from fansync.Exceptions import AuthFailed
from fansync.device_factory import DeviceFactory
from fansync.websocket import *






class FanSync:
    API_URL = "https://fanimation.apps.exosite.io"
    CREDENTIALS_FILE = ".fansync-credentials"

    def __init__(self):
        self._id = 1
        self._status = {}
        self._websocket = None
        self._device_factory: DeviceFactory = FanSync._get_device_factory()

    @staticmethod
    # TODO We should be able to heavily cache this
    def _get_device_factory() -> DeviceFactory:
        # GET https://fanimation.apps.exosite.io/api:1/info-model
        result: requests.Response = requests.get(FanSync.API_URL + '/api:1/info-model', headers=FanSync._get_headers())

        return DeviceFactory(result.json())

    @staticmethod
    def _get_headers(token= None):
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8"}

        if token:
            headers["Authorization"] = "Bearer %s" % token

        return headers

    @staticmethod
    def _load_cached_credentials() -> Optional[Credentials]:
        print("Trying to load cached credential token...", end="")
        _id = None
        _token = None
        if os.path.exists(FanSync.CREDENTIALS_FILE):
            with open(FanSync.CREDENTIALS_FILE) as cred_file:
                try:
                    json_data = json.loads(cred_file.read())
                    _id = int(json_data["id"])
                    _token = json_data["token"]
                except JSONDecodeError:
                    print("Cached credentials file invalid")
                    return None

        if _id and _token:
            print("success!")
            return Credentials(id=_id, token=_token)

        print("failed")
        return None

    @staticmethod
    def _save_cached_credentials(creds: Credentials):
        with open(FanSync.CREDENTIALS_FILE, "w") as creds_file:
            creds_file.write(json.dumps(creds.model_dump()))

    @staticmethod
    def _validate_token(params: Credentials):
        headers = FanSync._get_headers(params.token)

        result = requests.get(FanSync.API_URL + '/api:1/session', headers=headers)

        if result.status_code != 200:
            raise AuthFailed(f"Token validation return {result.status_code}")

        return "valid" == result.json()["status"]

    def _get_network_credentials(self, email: str, password: str) -> Optional[Credentials]:
        print("Getting network credentials")
        r = requests.post(self.API_URL + '/api:1/session',
                          json={"email": email, "password": password})

        if r.status_code != 200:
            print("Failed to login")
            raise AuthFailed()

        ret = r.json()
        _id = int(ret["id"])
        _token = ret["token"]

        print(f"Got login data: {ret}")

        return Credentials(id=_id, token=_token)

    # def _options_auth(self):
    #     options_headers = {
    #         # "access-control-request-method": "POST",
    #         # "origin": "http://localhost",
    #         # "access-control-request-headers": "content-type"
    #     }
    #
    #     options = self._client.options(self.API_URL + '/api:1/session',
    #                                    headers=options_headers)
    #     if options.status_code != 200:
    #         raise AuthFailed("Failed to set login OPTIONS")

    def open(self, email, password):

        creds = FanSync._load_cached_credentials()
        if creds:
            token_is_valid = self._validate_token(creds)
            print(f"Token is{'' if token_is_valid else ' not'} valid")
        else:
            creds = self._get_network_credentials(email, password)

        if not creds:
            raise ValueError("Could not get credentials")

        FanSync._save_cached_credentials(creds)
        self._websocket = Websocket(creds, self._device_factory)
        self._websocket.run()

    def run(self):
        pass

        return

        asyncio.run(self._websocket.run())

        # self._websocket.connect()

        # self._websocket.start()

        # for device in self._websocket.list_devices():
        #     pass





