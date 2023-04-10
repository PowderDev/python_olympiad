import csv
import os
import contextlib
from typing import IO, Generator
from pathlib import Path

from NetworkValidator import network_validator
from NetworkResolver import network_resolver
from Logger import logger
from utils.exceptions.networkExceptions import (
    InvalidHostException,
    InvalidPortException,
)
from utils.exceptions.parseExceptions import CSVHostsParseException
from utils.dataclasses.host import Host


class HostsCsvParser:
    @contextlib.contextmanager
    def open_file(self, file_path: Path) -> Generator[IO, None, None]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Provided file '{file_path}' not found")

        file = open(file_path, "r", encoding="utf-8")
        yield file
        file.close()

    def parse(self, file_path: Path) -> list[Host]:
        hosts = []

        with self.open_file(file_path) as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)  # To skip the first line

            for line in csv_reader:
                host = self.populate_and_validate_line(line)
                hosts.append(host)

        return hosts

    def populate_and_validate_line(self, line: list[str]) -> Host:
        ports = line[1].split(",")
        host = line[0]

        try:
            valid_port_numbers = network_validator.validate_ports(ports)
        except InvalidPortException as err:
            logger.log_port_error(err.port)
            raise CSVHostsParseException

        try:
            (domain, ip_addresses) = network_resolver.populate_host(host)
        except InvalidHostException as err:
            logger.log_host_error(err.host)
            raise CSVHostsParseException

        return Host(domain, ip_addresses, valid_port_numbers)


hosts_parser = HostsCsvParser()
