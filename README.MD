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

## Testing Challenges
There are some kind of limits in place for these API's.  Because none of this
is documented, it's a lot of trying to figure out and guess what's going on.
During parts of my testing, I'm getting no response from the websocket 
`login` request.  I'm able to get past it (sometimes) when needed, but it 
seems to crop up out of nowhere.

Additionally, the phone apps don't seem to be affected by this.  There are
still variances between the phone functionality, such as TLS and HTTP
versions.  Calling the API's in just the right order with the right timings
(I don't suspect a variation on [port knocking](https://en.wikipedia.org/wiki/Port_knocking)
at this point in time)

# Protocol
As it stands, the protocol is split into https REST API's as well as secure 
websockets for "real time" command and control.  Let's dig in.

## Overview
TLS certificate trust need to be disabled for the connections. I didn't
dig into this too much, but that's the lay of the land.



## REST

The following is a list of the API's discovered so far

| HTTP Verb | Auth? | Description                                                                                                    | URL                                                                      |
|-----------|-------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| GET       | No    | Retrieve progamatic logic for managing devices                                                                 | https://fanimation.apps.exosite.io/api:1/info-model                      |
| OPTIONS   | No    | Pre-flight authorization setup to retrieve list of firmware for a given device.  Not required?                 | https://fanimation.apps.exosite.io/api:1/fw/list/[<device-name>]    [^1] |
| GET       | No    | Retrieve list of firmware for a given device                                                                   | https://fanimation.apps.exosite.io/api:1/fw/list/[<device-name>]    [^1] |
| OPTIONS   | No    | Part of the auth sequence.  Seems to be something<br/>used for pre-flight of the auth sequence.  Not required? | https://fanimation.apps.exosite.io/api:1/session                         |
| GET       | Yes   | Part of the auth sequence.  Used to validate token                                                             | https://fanimation.apps.exosite.io/api:1/session                         |
| POST      | No    | Part of the auth sequence.  Used to retrieve token                                                             | https://fanimation.apps.exosite.io/api:1/session                         |

UI / App related URL's

| HTTP Verb | Auth? | Description                               | URL                                                           |
|-----------|-------|-------------------------------------------|---------------------------------------------------------------|
| GET       | No    | Get navbar logo                           | https://fanimation.apps.exosite.io/theme/logo_navbar.png [^2] |
| GET       | No    | Get fanimation logo                       | https://fanimation.apps.exosite.io/theme/logo.png             |
| GET       | No    | Get text values for various UI components | https://fanimation.apps.exosite.io/api:1/theme  [^3]          |


[^1]: For example: https://fanimation.apps.exosite.io/api:1/fw/list/[\"OdynCustom-FDR1L2\"]

[^2]: Not functional at time of writing

[^3]: Total speculation - This could be internationalization enabled via `accept-language` header?


### OPTIONS /api:1/session - Pre-flight of authorization request

This doesn't strictly seem to be required.  I've not used this and also used it.  It doesn't seem to make a difference.

Sniffed traffic:
```
        Header: :method: OPTIONS
        Header: :authority: fanimation.apps.exosite.io
        Header: :scheme: https
        Header: :path: /api:1/session
        Header: accept: */*
        Header: access-control-request-method: GET
        Header: access-control-request-headers: authorization,content-type
        Header: origin: http://localhost
        Header: user-agent: <USER-AGENT>
        Header: sec-fetch-mode: cors
        Header: x-requested-with: com.fanimation.fanSyncW
        Header: sec-fetch-site: cross-site
        Header: sec-fetch-dest: empty
        Header: referer: http://localhost/
        Header: accept-encoding: gzip, deflate, br
        Header: accept-language: en-US,en;q=0.9
        [Full request URI: https://fanimation.apps.exosite.io/api:1/session]
```

### POST /api:1/session - Getting Authentication Token


#### Basic Authentication
This deals with authenticating to the Fanimation / FanSync service itself.  A plain old username@domain.com email
address.  Not w/ Facebook or anything else.  
The login process appears to be a two-phase approach.  First you fire off an
`OPTIONS` request (although it doesn't appear to be strictly required) and then
you `POST` a blob w/ your email/password and get back a token and an ID.

The ID does not appear to be used anywhere.  It's not used on the websocket side of the house.  When
the websocket connects, the ID count starts at 1 and increments from there.  

`POST https://fanimation.apps.exosite.io/api:1/session`

Request Body:
```
{
    "email": "<EMAIL>@<DOMAIN>.com",
    "password": "<PASSWORD-IN-APP>"
}
```

Response:
```json5
{
    "id": "12345",   // Numeric USER ID
    "token": "[BASE-64 JWT TOKEN]"
}
```

##### Sample Decoded Token
Appears to be a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token).  The fields
should be referenced from the wiki, but I'll annotate interesting things.  Note, the 
clients don't appear to introspect this token at all.  Huh..

**Header**
{"typ":"JWT","alg":"HS256"}

**Payload**
```json5
{
  "sub": 12345, // Numeric USER ID
  "iss":"http://sphinx-usm:4070/api/v1/user/login", // Some internal URL?
  "iat":1691960382, // unix epoch time in seconds
  "exp":1694552382, // unix epoch time in seconds
  "nbf":1691960382, // unix epoch time in seconds
  "jti":"[PURPOSEFULLY OMITTED]"
}

```
**Signature**
```PURPOSEFULLY OMITTED```

This is kept for clarity.  I omitted this, because it has sensitive info. This appeared
to be binary data, which makes sense for what the spec says it is.



#### SSO Authentication
There is the ability to login using Facebook, Google, and other auth providers.  I haven't explored how to do this yet.



## Websocket

List of known values for `request` field in JSON 

| id                | C/R/U/D | Description                                           |
|-------------------|---------|-------------------------------------------------------|
| `provision_token` | Update  | Looks like it's used at some points right after login |
| `get_me`          | Read    | TBD                                                   |
| `config`          | TBD     | TBD                                                   |
| `set`             | Update  | Set device field values                               |
| `get`             | READ    | Get device information                                |
| `ota`             | TBD     | TBD                                                   |
| `calendar`        | TBD     | TBD                                                   |
| `add_user`        | Create? | TBD                                                   |
| `add_user_verify` | TBD     | TBD                                                   |
| `add_user`        | TBD     | TBD                                                   |
| `rem_user`        | TBD     | TBD                                                   |
| `lst_user`        | TBD     | TBD                                                   |
| `lst_device`      | Read    | List all devices in the account                       |
| `set_properties`  | TBD     | TBD                                                   |
| `del_properties`  | TBD     | TBD                                                   |
| `del_device`      | TBD     | TBD                                                   |
| `set_group`       | TBD     | TBD                                                   |
| `get_group`       | TBD     | TBD                                                   |
| `del_group`       | TBD     | TBD                                                   |
| `lst_group`       | Read    | List device groups?                                   |
| `set_user_data`   | TBD     | TBD                                                   |
| `del_user_data`   | TBD     | TBD                                                   |
| `get_user_data`   | TBD     | TBD                                                   |

### Note on Request ID's

Request id's are monotonically updated for each request, and the corresponding response
has the request id reflected in it.  This does allow for multi-threaded apps
to be able to tie a given request-response pair, but it really feels cumbersome.
IDK.  I think a likely takeaway is "don't issue too many commands at a time".



### Request
It's a request.  You give it an `id` in the request the type of `request` it 
is, and then any `data` required.  Look at the [models](fansync/models/__init__.py)
for the code that documents this better.


### Response
The response will have the `id` and the type of `response` it was. It will
finally have a `status` (of which, I've only observed `ok`)


### Event
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
```json5
{
  "data": {
      "changes": {
          // These appear to be mapped differently per device, so you'll need to translate these
          "status": {
              "H01":0,
              "H05":0,
              "H0D":0,
              "H06":0,
              "H0E":0,
              "H0B":0,
              "H00":1,
              "H0C":82,
              "H02":86
            }
        },
      "device":"<device_id>"
  },
  "event":"device_change"
}
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

[Sample Output](./test/http/info-model.json)


# RAW Notes
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
