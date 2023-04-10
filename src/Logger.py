import logging
import logging.config
from pathlib import Path

from utils.helperDecorators import skip_nones_in_kwargs
from utils.dataclasses.host import HostResolveInfo


class SimpleLogger:
    def __init__(self, config_path: Path):
        logging.config.fileConfig(config_path)
        self.root_logger = logging.getLogger("root_logger")
        self.host_logger = logging.getLogger("host_logger")

        # delimiter between hosts resolutions
        self.delimiter_logger = logging.getLogger("delimiter_logger")
        self.delimiter_logger.info("\n\n Stating resolving provided hosts... \n")

    @skip_nones_in_kwargs
    def log_host_info(self, info: HostResolveInfo) -> None:
        self.host_logger.info(f"\n['{info.domain}', {info.ip_addresses}, {info.ports}]")

    @skip_nones_in_kwargs
    def log_request(
        self,
        info: HostResolveInfo,
        domain="???",
    ) -> None:
        self.root_logger.info(
            f"'{domain}' | {info.ip_address} | {info.rtt} ms | {info.port} | {info.port_status.value}"
        )

    def log_host_error(self, domain_or_address: str) -> None:
        self.root_logger.error(
            f"Error: '{domain_or_address}' is an invalid domain name or ip address"
        )

    def log_port_error(self, port: str) -> None:
        self.root_logger.error(f"Error: port '{port}' is an invalid port number")

    def log_ping_failure(self, ip_address: str) -> None:
        self.root_logger.error(
            f"Error: failure occured while doing 'ping' to {ip_address}"
        )


logger = SimpleLogger(Path(__file__).parent.parent.joinpath("logging.conf"))
