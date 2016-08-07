#!/usr/bin/python
from os import popen

ifconfig = popen("ifconfig").read()
ips = []
for line in ifconfig.split("\n"):
	if "inet" in line:
		value = line.split()[1][5:]
		if value != "127.0.0.1":
			ips.append(value)
for ip in ips:
    print(ip)	 
