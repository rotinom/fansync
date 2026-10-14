"""Public interface for the FanSync client library."""

from open_fansync.exceptions import (
    AuthFailed,
    TimedOutException,
    WebsocketAlreadyConnectedException,
    WebsocketAuthException,
)
from open_fansync.http_api import HttpApi
from open_fansync.models import (
    Credentials,
    GetDeviceResponse,
    ListDevicesResponse,
    LoginResponse,
    Response,
)
from open_fansync.websocket import Websocket

__all__ = [
    "AuthFailed",
    "TimedOutException",
    "WebsocketAlreadyConnectedException",
    "WebsocketAuthException",
    "HttpApi",
    "Credentials",
    "GetDeviceResponse",
    "ListDevicesResponse",
    "LoginResponse",
    "Response",
    "Websocket",
]
