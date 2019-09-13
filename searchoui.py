#!/usr/bin/python
import requests
import sys

web = "https://api.macvendors.com/" + sys.argv[1]


vendor = requests.get(web).text

print(vendor)
