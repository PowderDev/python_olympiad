import csv
import socket

from utils.network_validators import (
    validate_domain_name,
    validate_ip_address,
    validate_port_number,
)
from SimpleLogger import logger


class HostsCsvParser:
    def parse(self, filepath):
        hosts = []

        with open(filepath, "r") as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)

            for line in csv_reader:
                try:
                    formatted_line = self.populate_and_validate_line(line)
                    hosts.append(formatted_line)
                except ValueError:
                    print(
                        f"Error ocurred when parsing {filepath}. Please check the output.log file"
                    )
                    exit(1)

        return hosts

    def populate_and_validate_line(self, line):
        ports = line[1].split(",")
        valid_port_numbers = self.validate_ports(ports)
        (domain, ip_addresses) = self.get_domain_and_address(line[0])
        return (domain, ip_addresses, valid_port_numbers)

    def get_domain_and_address(self, domain_or_address):
        domain = ""
        ip_addresses = []

        if validate_domain_name(domain_or_address):
            domain = domain_or_address
        elif validate_ip_address(domain_or_address):
            ip_addresses = [domain_or_address]
        else:
            logger.log_destination_domain_or_address_error(domain_or_address)
            raise ValueError

        if domain:
            res = socket.gethostbyname_ex(domain)
            ip_addresses = res[2]

        return (domain, ip_addresses)

    def validate_ports(self, ports):
        port_numbers = []
        for port in ports:
            if port == "":
                continue

            if validate_port_number(port):
                port_numbers.append(int(port))
            else:
                logger.log_destination_port_error(port)
                raise ValueError
        return port_numbers


hosts_parser = HostsCsvParser()
