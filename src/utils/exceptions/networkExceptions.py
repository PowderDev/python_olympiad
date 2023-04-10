class InvalidPortException(Exception):
    def __init__(self, message="Invalid port was provided", port=""):
        super().__init__(message)
        self.port = port
        self.message = message


class InvalidHostException(Exception):
    def __init__(self, message="Invalid host was provided", host=""):
        super().__init__(message)
        self.host = host
        self.message = message


class PingFailureException(Exception):
    def __init__(self, message="Failure occured while doing ping", ip_address=""):
        super().__init__(message)
        self.ip_address = ip_address
        self.message = message


class PingPermissionDeniedException(Exception):
    def __init__(self, message="This app don't have the permission to do 'ping'"):
        super().__init__(message)
        self.message = message
