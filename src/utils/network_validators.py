import re
import socket


def validate_domain_name(domain_name):
    pattern = re.compile(
        r"^localhost|((((?!\-))(xn\-\-)?[a-z0-9\-_]{0,61}[a-z0-9]{1,1}\.)*(xn\-\-)?([a-z0-9\-]{1,61}|[a-z0-9\-]{1,30})\.[a-z]{2,})$"
    )

    if pattern.fullmatch(domain_name):
        return True
    else:
        return False


def validate_ip_address(ip_address):
    pattern = re.compile("^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$")

    if pattern.fullmatch(ip_address):
        return True
    else:
        return False


def validate_port_number(port):
    try:
        port_number = int(port)
        if port_number > 0 and port_number < 65535:
            return True
        else:
            return False

    except ValueError:
        return False


def validate_internet_connection():
    ip_address = socket.gethostbyname(socket.gethostname())

    if ip_address == "127.0.0.1":
        return False
    else:
        return True
