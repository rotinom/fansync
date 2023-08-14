
import os
from json import JSONDecodeError


from fansync.Exceptions import AuthFailed
from fansync.device_factory import DeviceFactory
from fansync.websocket import *






class FanSync:
    API_URL = "https://fanimation.apps.exosite.io"
    CREDENTIALS_FILE = ".fansync-credentials"
    MAX_AUTH_RETRIES = 3

    def __init__(self):
        self._id = 1
        self._status = {}
        self._websocket = None

        # TODO Move this.  Shouldn't be here.
        self._device_factory: DeviceFactory = FanSync._get_device_factory()

    @staticmethod
    # TODO We should be able to heavily cache this
    # TODO Move this
    def _get_device_factory() -> DeviceFactory:
        # GET https://fanimation.apps.exosite.io/api:1/info-model
        result: requests.Response = requests.get(FanSync.API_URL + '/api:1/info-model', headers=FanSync._get_headers())

        return DeviceFactory(result.json())

    @staticmethod
    def _get_headers(token=None):
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8"}

        if token:
            headers["Authorization"] = "Bearer %s" % token

        return headers

    # TODO Move this.  This is an application concern, not a socket concern
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

    # TODO Move this.  This is an application concern, not a socket concern
    @staticmethod
    def _save_cached_credentials(creds: Credentials):
        with open(FanSync.CREDENTIALS_FILE, "w") as creds_file:
            creds_file.write(json.dumps(creds.model_dump()))

    @staticmethod
    def _get_session_token_is_valid(params: Credentials):
        headers = FanSync._get_headers(params.token)

        result = requests.get(FanSync.API_URL + '/api:1/session', headers=headers)

        if result.status_code != 200:
            raise AuthFailed(f"Token validation return {result.status_code}")

        return "valid" == result.json()["status"]

    def _post_network_credentials(self, email: str, password: str) -> Optional[Credentials]:
        print("POST'ing network credentials")

        j = HttpCredentials(email=email, password=password).model_dump_json()
        print(j)

        r = requests.post(self.API_URL + '/api:1/session',
                          json=j, headers=FanSync._get_headers())

        if r.status_code != 200:
            msg = f"Failed to login, {r.reason}({r.status_code})"
            raise AuthFailed(msg)

        ret = r.json()
        _id = int(ret["id"])
        _token = ret["token"]

        print(f"Got login data: {ret}")

        return Credentials(id=_id, token=_token)

    def _login(self, email: str, password: str) -> Optional[Credentials]:
        print("Auth token")
        r = requests.post(self.API_URL + '/api:1/session',
                          headers=FanSync._get_headers(),
                          json={"email": email, "password": password})

        if r.status_code != 200:
            msg = f"Failed to login, {r.reason}({r.status_code})"
            raise AuthFailed(msg)

        ret = r.json()
        _id = 0  # int(ret["id"])
        _token = ret["token"]

        print(f"Got auth data: {ret}")

        return Credentials(id=_id, token=_token)



    # def _get_network_credentials(self, email: str, password: str) -> Optional[Credentials]:
    #     print("GET'ing network credentials")
    #     r = requests.get(self.API_URL + '/api:1/session',
    #                      json=HttpCredentials(email=email, password=password).model_dump_json())
    #
    #     if r.status_code != 200:
    #         msg = f"Failed to login, {r.reason}({r.status_code})"
    #         raise AuthFailed(msg)
    #
    #     ret = r.json()
    #     _id = int(ret["id"])
    #     _token = ret["token"]
    #
    #     print(f"Got login data: {ret}")
    #
    #     return Credentials(id=_id, token=_token)

    def _preflight_session(self):
        options_headers = {
            "access-control-request-method": "GET",
            "access-control-request-headers": "authorization,content-type",
            "origin": "http://localhost",
            "referer": "http://localhost",
        }

        options = requests.options(f"{self.API_URL}/api:1/session",
                                   headers=options_headers)
        if options.status_code != 200:
            raise AuthFailed("Failed to set login OPTIONS")

    # def _authenticate(self):
    #     self._optionsSession()
    #     self._getSession()  # Got 403 Forbidden
    #
    #
    #
    # def _optionsSession(self):
    #     pass

    def open(self, email, password):

        # Try and load token from disk. If we can, use it. If we can't then get it from HTTP
        creds = FanSync._load_cached_credentials()
        # if creds:

            # We do this if we are doing a "cold" auth, not a "warm" auth
            # is_valid = self._get_session_token_is_valid(creds)
            # print(f"Token is{'' if is_valid else ' not'} valid")
        # else:

        if not creds:
            self._preflight_session() # Preflight the authentication
            creds = self._login(email, password)




        # Our authentication loop
        for i in range(0, FanSync.MAX_AUTH_RETRIES):
            if not creds:
                raise ValueError("Could not get credentials")

            # Create and login our websocket
            try:
                self._websocket = Websocket(creds, self._device_factory)
                break

            # Uh-oh, login failed.  Let's regroup here.
            except WebsocketAuthException:
                # Well, websocket couldn't auth.  Try and get a new token?
                creds = self._login(email, password)

            if i >= (FanSync.MAX_AUTH_RETRIES-1):
                raise AuthFailed()

        # Save the credentials we finally got
        FanSync._save_cached_credentials(creds)
        self._websocket.run()

    def close(self):
        self._websocket.close()

    def run(self):
        pass

        return

        asyncio.run(self._websocket.run())

        # self._websocket.connect()

        # self._websocket.start()

        # for device in self._websocket.list_devices():
        #     pass





