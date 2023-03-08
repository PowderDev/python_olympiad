from pythonping import ping

import socket

from utils.RTT import get_RTT
from SimpleLogger import logger


class Request:
    def attempt(self, hosts):
        for host in hosts:
            domain = host[0]
            ip_addresses = host[1]
            ports = host[2]

            logger.log_destination(domain, ip_addresses, ports)

            for ip_address in ip_addresses:
                if len(ports) > 0:
                    for port in ports:
                        (port_status, rtt) = self.check_socket(ip_address, port)
                        logger.log_request(
                            ip_address,
                            rtt,
                            domain_name=domain,
                            port=port,
                            port_status=port_status,
                        )
                else:
                    (_, rtt) = self.ping_address(ip_address)
                    logger.log_request(
                        ip_address,
                        rtt,
                        domain_name=domain,
                    )

    @get_RTT
    def check_socket(self, ip_address, port):
        port_status = None
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            port_status = "Open"
        sock.close()
        return port_status

    @get_RTT
    def ping_address(self, ip_address):
        ping(ip_address, timeout=1)


request = Request()
