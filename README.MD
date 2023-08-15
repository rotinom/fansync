# FanSync Cloud API

This is a reverse engineered version of the Fanimation FanSync API.  It works as of now, 
but since this is undocumented, it's really up to them as to whether they'll break
it.  If it does break, feel free to send a patch. 

## Why?
I like their fans, and I use HA.  It seems like peanut butter and chocolate that
go together.  I think their add-on controllers are ideally placed to smart-ify
any dumb fan, especially light-fan combos that are only installed where a single
conductor is available.  These are common in bedrooms and are super problematic
when you want a youngster to be able to have control of their own light and fan
separately.

*Author Notes: I write informally.  Shoot me.  I'm not super happy with formatting of
this, but I'm trying to brain dump so that this information is at least out
there.  I'll be vague on some things, but hopefully nothing super important.
I haven't explored all API's, but I'm focusing on the ones to enable basic
on-off control of the features of a fan-light combo.  Anything else comes
after that.*


## Install
* Requires python 3 installed. Follow instructions to make that happen from 
  python.org
  * `pip3 install websocket-client`


## Protocol
As it stands, the protocol is split into https REST API's as well as secure 
websockets for "real time" command and control.  Let's dig in.

### Note on TLS
It appears that the TLS certificates in use are not to be trusted.  I didn't
dig into this too much, but that's the lay of the land.

### Note on Request ID's
I'm not SUPER experienced w/ websockets and front-end coding, but their 
request/response framework is a bit weird to me.  Maybe it makes more sense
if I was.  My gut tells me that a lot of this was done using the async/await
paradigm, but my brain doesn't work that way as of yet.  I'm going w/ a 
"traditional" threads approach w/ my POC.  

I *think* that the initial ID for a session is handed to the client via the 
`id` field in the LOGIN response.  This doesn't appear to be strictly required either.

Request id's are monotonically updated for each request, and the corresponding response
has the request id reflected in it.  This does allow for multi-threaded apps
to be able to tie a given request-response pair, but it really feels cumbersome.
IDK.  I think a likely takeaway is "don't issue too many commands at a time".

Websocket messages are split into at least three categories:
* Request
* Response
* Event

#### Request
It's a request.  You give it an `id` in the request the type of `request` it 
is, and then any `data` required.  Look at the [models](fansync/models/__init__.py)
for the code that documents this better.

Sample:
```
{"id":8,"request":"set","device":"<device_id>","data":{"H00":1}}
```

#### Response
The response will have the `id` and the type of `response` it was. It will
finally have a `status` (of which, I've only observed `ok`)

**Sample**
```
{"status":"ok","response":"set","id":8}
```

#### Event
When a change is requested from client -> server, the response to the request
is given (as shown above).  In addition to this, a server-side event is also
fired (presumably to all connected clients) to allow them to update their 
client-side views with the up-to-date data.  Evidence of this can be seen in
the phone app, where a change is made (in my case, often setting the fan to 
100%), and then the fan "jumping" back to some other "maximum" value (such as 
87%). The first change is the client locally updating the view to the data sent
in the `set` request, and the latter is the server-side update event actually
reflecting 'reality'.

**Sample**
```
{"data":{"changes":{"status":{"H01":0,"H05":0,"H0D":0,"H06":0,"H0E":0,"H0B":0,"H00":1,"H0C":82,"H02":86}},"device":"<device_id>"},"event":"device_change"}
```




### HTTPS REST

##### /info-model
**URI**
`GET https://fanimation.apps.exosite.io/api:1/info-model`

**Auth required** No

**Description**
This API appears to be used to describe the capabilities of each of their 
networked products in a JSON format.  IMHO, this is pretty clever, as it 
allows them to launch a new product with new abilities, without having to launch
a new phone app.

I haven't decoded this extensively, but first glance has it have some REGEX 
like expressions that you can run against the model numbers in your account in
order to figure out what JSON blob belongs with your device.  Like I said, 
pretty slick.

Decoding this in a basic manner will open up control of all FanSync hardware.

<u>Edit 1</u> - *Good grief, it's Javascript based*

<u>Edit 2</u> - *There is no god.*

[Sample Output](./docs/fw-list.md)



#### /fw/list
**URI** 
`GET https://fanimation.apps.exosite.io/api:1/fw/list/[%22OdynCustom-FDR1L2%22]`

**Description**
This appears to return a list of the firmware available for the given model.
Not totally sure where this model name comes from, but it's there.

<details>

  <summary>Sample Output</summary>

```
[
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS42LjV8MS42LjN8ZGU4YzAxYjBiZGU5YTE3NjI4MmE2OWI1NmYwMTA5ODdhODlhNDMzZHxPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.6.5",
    "size": 403638,
    "previousVersion": "1.6.3",
    "sha1": "de8c01b0bde9a176282a69b56f010987a89a433d",
    "name": "MS42LjV8MS42LjN8ZGU4YzAxYjBiZGU5YTE3NjI4MmE2OWI1NmYwMTA5ODdhODlhNDMzZHxPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS43LjF8MS42LjV8MjM2NGYwZTc4NWQ1NzJkNThkMzk5NTJmMTdkNmRkOWExMzQ3NzA5Y3xPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.7.1",
    "size": 404150,
    "previousVersion": "1.6.5",
    "sha1": "2364f0e785d572d58d39952f17d6dd9a1347709c",
    "name": "MS43LjF8MS42LjV8MjM2NGYwZTc4NWQ1NzJkNThkMzk5NTJmMTdkNmRkOWExMzQ3NzA5Y3xPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS43LjF8MS42LjR8MjM2NGYwZTc4NWQ1NzJkNThkMzk5NTJmMTdkNmRkOWExMzQ3NzA5Y3xPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.7.1",
    "size": 404150,
    "previousVersion": "1.6.4",
    "sha1": "2364f0e785d572d58d39952f17d6dd9a1347709c",
    "name": "MS43LjF8MS42LjR8MjM2NGYwZTc4NWQ1NzJkNThkMzk5NTJmMTdkNmRkOWExMzQ3NzA5Y3xPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS42LjJ8MS42LjF8YmRkMzk3YzFmNDExZDVjNjQ4MzUzOTAyZGE4NDc5MjYzNDkyMGMwNnxPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.6.2",
    "size": 404110,
    "previousVersion": "1.6.1",
    "sha1": "bdd397c1f411d5c648353902da84792634920c06",
    "name": "MS42LjJ8MS42LjF8YmRkMzk3YzFmNDExZDVjNjQ4MzUzOTAyZGE4NDc5MjYzNDkyMGMwNnxPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS42LjN8MS42LjJ8YWUzMTM1OGUxMmU5NTVjMmRhY2U2MjY3NmU2ODVlMjAyZGY4MDhjNXxPZHluQ3VzdG9tLUZEUjFMMnx0cmlnZ2Vy",
    "version": "1.6.3",
    "size": 404566,
    "previousVersion": "1.6.2",
    "sha1": "ae31358e12e955c2dace62676e685e202df808c5",
    "name": "MS42LjN8MS42LjJ8YWUzMTM1OGUxMmU5NTVjMmRhY2U2MjY3NmU2ODVlMjAyZGY4MDhjNXxPZHluQ3VzdG9tLUZEUjFMMnx0cmlnZ2Vy",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS42LjF8MS4yLjZ8OTkwYTc3NTY5YzI4MDZmZDNjMDg3ZDJlYTU1YmI3ZjU2Mjk3ZWYwOHxPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.6.1",
    "size": 407054,
    "previousVersion": "1.2.6",
    "sha1": "990a77569c2806fd3c087d2ea55bb7f56297ef08",
    "name": "MS42LjF8MS4yLjZ8OTkwYTc3NTY5YzI4MDZmZDNjMDg3ZDJlYTU1YmI3ZjU2Mjk3ZWYwOHxPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  },
  {
    "url": "https://fanimation.apps.exosite.io/fw/content/MS42LjF8MS40LjB8OTkwYTc3NTY5YzI4MDZmZDNjMDg3ZDJlYTU1YmI3ZjU2Mjk3ZWYwOHxPZHluQ3VzdG9tLUZEUjFMMg",
    "version": "1.6.1",
    "size": 407054,
    "previousVersion": "1.4.0",
    "sha1": "990a77569c2806fd3c087d2ea55bb7f56297ef08",
    "name": "MS42LjF8MS40LjB8OTkwYTc3NTY5YzI4MDZmZDNjMDg3ZDJlYTU1YmI3ZjU2Mjk3ZWYwOHxPZHluQ3VzdG9tLUZEUjFMMg",
    "model": "OdynCustom-FDR1L2"
  }
]
```

</details>

#### Login

**Description**
The login process appears to be a two-phase approach.  First you fire off an
`OPTIONS` request (although it doesn't appear to be strictly required) and then
you `POST` a blob w/ your email.password and get back a token and an ID

`POST https://fanimation.apps.exosite.io/api:1/session`

Request Body:
```
{
    "email": "<EMAIL>@<DOMAIN>.com",
    "password": "<PASSWORD-IN-APP>"
}
```

Response:
```
{
    "id": "XXXXX",   // Some numeric value
    "token": "ey<SOME VALUE>"
}
```

Websocket connect
`wss://fanimation.apps.exosite.io:443/api:1/phone`


Request:
```
{"id":1,"request":"login","data":{"token":"<login token>"}}
```

Response:
```
{"status":"ok","response":"login","id":1}
```

Websocket connection is now authorized, we're connected and ready to roll.

We then need to list some things to get the devices in our account.  The real phone app pulls
down  configuration stuff which is really boring to us in the HA world, so I'll gloss
over it for now.  We see:

```
# Not needed?
{"id":2,"request":"provision_token","data":{"expires_in":2592000}}

# We need this
{"id":3,"request":"lst_device"}

# FanSync group configs?  IDK, I don't use it.  Boring...
{"id":4,"request":"lst_group"}

# Get info about the user.  Again, boring from a HA perspective
{"id":5,"request":"get_user_data"}

# Big yawn-fest too.  Personal data. Config stuff for Alexa and IFTTT, but boring
# for HA to use
{"id":6,"request":"get_me"}
```


`lst_device` response:

*This appears to return a list of all the devices in the account.  This would then be used
as input to the `get` request*
```
{
  "status": "ok",
  "response": "lst_device",
  "data": [
    {
      "owner": "<owner_email_addr>",
      "device": "<device_id>",
      "properties": {
        "displayName": "<Fan Display Name In App>",
        "deviceHasBeenConfigured": true,
        "ignoreUpdateVersion": "1.7.1"
      },
      "role": "owner"
    }
  ],
  "id": 3
}
```
