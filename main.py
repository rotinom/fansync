import httpx
from SECRETS import LOGIN_JSON

client = httpx.Client(http2=True)

# Login
r = client.post('https://fanimation.apps.exosite.io/api:1/session', json=LOGIN_JSON)
print(r)
print(r.json())

r = client.get('https://fanimation.apps.exosite.io/api:1/')
print(r)
print(r.json())


# https://fanimation.apps.exosite.io/api:1/fw/list/[]  OPTIONS  ?   GET ?

# https://fanimation.apps.exosite.io/api:1/fw/list/[%22OdynCustom-FDR1L2%22]  GET ?  OPTIONS?    Auth not required?

# Get status of the session
# r = client.get('https://fanimation.apps.exosite.io/api:1/session')
# print(r)
# print(r.json())