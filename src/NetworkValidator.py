import re
import socket

from utils.exceptions.networkExceptions import InvalidPortException
from utils.validationConstants import DOMAIN_NAME_REGEX, IPV4_ADDRESS_REGEX


class NetworkValidator:
    @staticmethod
    def validate_domain_name(domain_name: str) -> bool:
        pattern = re.compile(DOMAIN_NAME_REGEX)

        if pattern.fullmatch(domain_name):
            return True
        else:
            return False

    @staticmethod
    def validate_ipv4_address(ip_address: str) -> bool:
        pattern = re.compile(IPV4_ADDRESS_REGEX)

        if pattern.fullmatch(ip_address):
            return True
        else:
            return False

    @staticmethod
    def validate_port_number(port: str) -> bool:
        try:
            port_number = int(port)
            if port_number > 0 and port_number < 65535:
                return True
            else:
                return False

        except ValueError:
            raise InvalidPortException(port=port)

    @staticmethod
    def validate_internet_connection() -> bool:
        ip_address = socket.gethostbyname(socket.gethostname())

        if ip_address == "127.0.0.1":
            return False
        else:
            return True

    @staticmethod
    def validate_ports(ports: list[str]) -> list[int]:
        port_numbers = []
        for port in ports:
            if port == "":
                continue

            if NetworkValidator.validate_port_number(port):
                port_numbers.append(int(port))
            else:
                raise InvalidPortException(port=port)

        return port_numbers

    @staticmethod
    def is_cert_to_check(port: int):
        return port == 443


network_validator = NetworkValidator()
