from pathlib import Path

from CSVParser import hosts_parser
from Request import request
from utils.network_validators import validate_internet_connection


def main():
    if not validate_internet_connection():
        print("You have no internet connection. Exiting...")
        exit(1)

    hosts = hosts_parser.parse(Path("./src", "csv", "hosts.csv"))
    request.attempt(hosts)
    print("Attempt was successful you can check out the output.log file now")


if __name__ == "__main__":
    main()
