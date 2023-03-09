import logging
from pathlib import Path

from utils.decorators import skip_nones_in_kwargs

logging.basicConfig(level=logging.DEBUG)


class SimpleLogger:
    def __init__(self, file_name="output.log"):
        self.logger = logging.getLogger("destination")
        self.handler = logging.FileHandler(
            Path(__file__).parent.parent.joinpath(file_name), mode="w"
        )
        self.logger.addHandler(self.handler)

    @skip_nones_in_kwargs
    def log_destination(self, domain_name="???", ip_addresses=[], ports=[]):
        domain_name = domain_name or "???"
        self.set_destination_format()
        self.logger.info(f"['{domain_name}', {ip_addresses}, {ports}]")

    @skip_nones_in_kwargs
    def log_request(
        self, ip_address, rtt, domain_name="???", port="-1", port_status="Unknown"
    ):
        domain_name = domain_name or "???"
        self.set_request_format
        self.logger.info(
            f"'{domain_name}' | {ip_address} | {rtt} ms | {port} | {port_status}"
        )

    def log_destination_domain_or_address_error(self, domain_or_address):
        self.set_destination_format()
        domain_or_address = f"'{domain_or_address}'"
        self.logger.error(
            f"Error: {domain_or_address} is an invalid domain name or ip address"
        )

    def log_destination_port_error(self, port):
        self.set_destination_format()
        port = f"'{port}'"
        self.logger.error(f"Error: port:{port} is an invalid port number")

    def set_destination_format(self):
        formatter = logging.Formatter("\n%(message)s \n")
        self.handler.setFormatter(formatter)

    def set_request_format(self):
        formatter = logging.Formatter("%(asctime)s | %(message)s\n")
        self.handler.setFormatter(formatter)


logger = SimpleLogger("output.log")
