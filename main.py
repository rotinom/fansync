#!./venv/bin/python

import time
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



try :
    f = FanSync()
    f.open(EMAIL, PASSWORD)



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





