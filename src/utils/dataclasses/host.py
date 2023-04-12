from dataclasses import dataclass
from typing import Union

from utils.enums.host import PortStatus
from utils.types.host import DOMAIN
from utils.enums.network import CertificateType


@dataclass
class Host:
    domain: DOMAIN
    ip_addresses: list[str]
    ports: list[int]


@dataclass
class HostResolveInfo:
    ip_address: str
    port: int
    port_status: PortStatus
    rtt: float
    cert_type: Union[CertificateType, None] = None
