#!/usr/bin/python

# Proxy Border by DaKnOb
# Complete rewrite

import requests
import threading
from random import choice
import sys

AlwaysOn = [
	"http://www.google.com",
	"http://www.youtube.com",
	"http://www.amazon.com",
	"http://www.apple.com",
	"http://www.microsoft.com",
	"http://www.samsung.com",
	"http://www.facebook.com",
	"http://www.twitter.com",
	"http://www.yahoo.com",
	"http://www.wikipedia.org",
	"http://www.akamai.com",
	"http://www.cloudflare.com"
]

def getRandomURL():
	return choice(AlwaysOn)

def checkProxy(ip, port):
	try:
		requests.get(
			getRandomURL(), 
			proxies = {'http': 'http://' + ip + ':' + str(port)},
			timeout = 5
		)
	except:
		writeNotWorkingProxyToOutput(ip, port)
		return
	writeWorkingProxyToOutput(ip, port)
	return

def writeWorkingProxyToOutput(ip, port):
	with open(Working, "a+") as out:
		out.write(ip + ":" + str(port) + "\n")
	return

def writeNotWorkingProxyToOutput(ip, port):
	with open(NotWorking, "a+") as out:
		out.write(ip + ":" + str(port) + "\n")
	return

# Main
try:
	Input = sys.argv[1]
	Working = sys.argv[2]
	NotWorking = sys.argv[3]
	MaxThreads = int(sys.argv[4])
except:
	print("Usage:")
	print("")
	print("proxyborder.py input.txt working.txt notworking.txt 32")
	print("\tinput.txt: A list of newline delimited proxies in the form of IP:PORT")
	print("\tworking.txt: The output file to append working proxies. Same format.")
	print("\tnotworking.txt: The output filr to append nonworking proxies. Same format.")
	print("\t32: The maximum amount of threads to spawn to check the proxy list.")
	print("Caveats:")
	print("\tSome proxies may appear as non-working because of slow response times.")
	print("\tWe suggest you run proxyborder again with the notworking.txt as input")
	print("\tand working.txt as output.")
	exit(1)

with open(Input, "r") as proxies:
	for proxy in proxies:
		p = proxy.replace("\n", "")
		p = p.split(":")
		while(threading.activeCount() >= MaxThreads):
			pass
		try:
			threading.Thread(target=checkProxy, args=(p[0], p[1])).start()
		except:
			print("Invalid Line:\t" + proxy)
