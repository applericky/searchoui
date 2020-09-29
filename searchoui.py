#!/usr/bin/env python3
import requests
import sys


def main():
    try:
        web = "https://api.macvendors.com/" + sys.argv[1]
        vendor = requests.get(web).text
        if "Not Found" in vendor:
            print("MAC address not found.")
        else:
            print(vendor)

    except IndexError as e:
        print("No MAC address entered.")


if __name__ == "__main__":
    main()
