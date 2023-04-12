from pythonping import ping
from time import time
import socket

from Logger import logger
from NetworkValidator import network_validator
from utils.exceptions.networkExceptions import (
    InvalidHostException,
    PingPermissionDeniedException,
    PingFailureException,
)
from utils.dataclasses.host import HostResolveInfo, Host
from utils.helpers import get_rrt
from utils.enums.host import PortStatus
from utils.types.host import DOMAIN


class NetworkResolver:
    def resolve_networks(self, hosts: list[Host], timeout: int):
        for host in hosts:
            logger.log_host_info(host)

            for ip_address in host.ip_addresses:
                if len(host.ports) > 0:
                    for port in host.ports:
                        host_resolve_info = self.check_socket_connection(
                            ip_address, port, timeout
                        )
                        logger.log_request(host_resolve_info, host.domain)
                else:
                    host_resolve_info = self.ping_address(ip_address, timeout)
                    logger.log_request(host_resolve_info, host.domain)

    def check_socket_connection(
        self, ip_address: str, port: int, timeout: int
    ) -> HostResolveInfo:
        start_time = time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip_address, port))
            port_status = PortStatus.OPENED if result == 0 else PortStatus.UNKNOWN

        rtt = get_rrt(start_time)

        return HostResolveInfo(
            ip_address=ip_address,
            port=port,
            port_status=port_status,
            rtt=rtt,
        )

    def ping_address(self, ip_address: str, timeout: int) -> HostResolveInfo:
        try:
            start_time = time()
            res = ping(ip_address, timeout, count=1)

            if not res.success():
                raise PingFailureException(ip_address=ip_address)

            rtt = get_rrt(start_time)

            return HostResolveInfo(
                ip_address=ip_address,
                port=1,
                port_status=PortStatus.OPENED,
                rtt=rtt,
            )

        except PermissionError:
            raise PingPermissionDeniedException

        except PingFailureException as err:
            logger.log_ping_failure(ip_address=err.ip_address)
            raise PingFailureException

    def populate_host(self, host: str) -> tuple[DOMAIN, str]:
        domain = None
        ip_addresses = []

        if network_validator.validate_domain_name(host):
            domain = host
        elif network_validator.validate_ipv4_address(host):
            ip_addresses = [host]
        else:
            raise InvalidHostException(host=host)

        if domain:
            res = socket.gethostbyname_ex(domain)
            ip_addresses = res[2]

        return (domain, ip_addresses)


network_resolver = NetworkResolver()
