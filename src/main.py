from pathlib import Path
import argparse
from time import sleep

from HostsParser import hosts_parser
from NetworkResolver import network_resolver
from NetworkValidator import network_validator

argparser = argparse.ArgumentParser()

argparser.add_argument("-inf", "--infinite", action="store_true", default=False)
argparser.add_argument("-int", "--interval", default=10, type=int)
argparser.add_argument("-t", "--timeout", default=1, type=int)
argparser.add_argument("-f", "--file", default="hosts.csv", type=str)

args = argparser.parse_args()


def main():
    try:
        if not network_validator.validate_internet_connection():
            print("You have no internet connection. Shutting down...")
            exit(1)

        hosts = hosts_parser.parse(args.file)
        network_resolver.resolve_networks(hosts, args.timeout)
        print("All hosts was successfully checked. To see, open the output.log")

    except Exception as err:
        if err.message:
            print(f"Error: {err.message}")
        else:
            print(err)
        exit(1)


def infinite_main_loop():
    while True:
        try:
            main()
            sleep(args.interval)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    if args.infinite:
        infinite_main_loop()
    else:
        main()
