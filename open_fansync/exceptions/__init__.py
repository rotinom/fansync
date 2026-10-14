

class AuthFailed (BaseException):
    pass


class WebsocketAuthException(Exception):
    pass

class WebsocketAlreadyConnectedException(Exception):
    pass


class TimedOutException(Exception):
    pass
