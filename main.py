#!./venv/bin/python

import time

import fansync
from fansync import websocket
from fansync import *
from SECRETS import *

# client = httpx.Client(http2=True)
#
# # Login
# r = client.post('https://fanimation.apps.exosite.io/api:1/session', json=LOGIN_JSON)
# print(r)
# print(r.json())
#

# Doesn't work
# r = client.get('https://fanimation.apps.exosite.io/api:1/')
# print(r)
# print(r.json())
#

# https://fanimation.apps.exosite.io/api:1/fw/list/[]  OPTIONS  ?   GET ?

# https://fanimation.apps.exosite.io/api:1/fw/list/[%22OdynCustom-FDR1L2%22]  GET ?  OPTIONS?    Auth not required?

# Get status of the session
# r = client.get('https://fanimation.apps.exosite.io/api:1/session')
# print(r)
# print(r.json())

CREDENTIALS_FILE = ".fansync-credentials"

def _load_cached_credentials() -> Optional[Credentials]:
    print("Trying to load cached credential token...", end="")
    _id = None
    _token = None
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE) as cred_file:
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



def _save_cached_credentials(creds: Credentials):
    with open(CREDENTIALS_FILE, "w") as creds_file:
        creds_file.write(json.dumps(creds.model_dump()))


try:

    # creds = _load_cached_credentials()

    h = HttpApi()

    h.options_session()
    credentials: Credentials = h.post_session(EMAIL, PASSWORD)
    h.get_session(credentials)

    if not credentials:
        raise AuthFailed()

    # w = fansync.Websocket(credentials.token)
    # w.connect()
    # w.login()



    # listDeviceResponse = f.ws_list_devices()
    # for i in range(100):
    #     time.sleep(0.5)
    #     for device in listDeviceResponse.data:
    #         f.ws_get_device(device)

    # time.sleep(100.0)
finally:
    pass
    # f.close()





# f.fuzz("https://fanimation.apps.exosite.io/api:1/fw/list/[]")

# Describes the capacities of the various fan/light combinations
# f.fuzz("https://fanimation.apps.exosite.io/api:1/info-model")

# List the firmware revisions for a given model
# f.fuzz("https://fanimation.apps.exosite.io/api:1/fw/list/[\"OdynCustom-FDR1L2\"]")





