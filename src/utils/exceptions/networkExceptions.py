class InvalidPortException(Exception):
    def __init__(self, port: str, message=""):
        self.message = message or f"Invalid port {port} was provided"
        self.port = port
        super().__init__(message)


class InvalidHostnameException(Exception):
    def __init__(self, hostname: str, message=""):
        self.message = message or f"Invalid hostname '{hostname}' was provided"
        self.hostname = hostname
        super().__init__(message)


class PingFailureException(Exception):
    def __init__(self, ip_address: str, message=""):
        self.message = message or f"Failure occured while doing ping to {ip_address}"
        self.ip_address = ip_address
        super().__init__(self.message)


class PingPermissionDeniedException(Exception):
    def __init__(self, message="This app don't have the permission to do 'ping'"):
        super().__init__(message)
        self.message = message
