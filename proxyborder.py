#!usr/bin/python
#ProxyBorder By DaKnOb

import urllib2	# Makes the tool work
import thread	# Makes the tool faster
import random	# Makes the tool evenly distributed 
import time	# Makes the tool friendlier
import string	# Makes the tool easier
import sys	# Makes the tool expandable

def getURLtoMakeRequest():
	
	#	Return a URL that is up most if not
	#	all of the time to request with a
	#	specific proxy that has to be tested.

        urls = []
        urls.append("http://www.google.com")
        urls.append("http://www.youtube.com")
	urls.append("http://www.amazon.com")
        urls.append("http://www.apple.com")
        urls.append("http://www.microsoft.com")
        urls.append("http://www.samsung.com")
        urls.append("http://www.facebook.com")
        urls.append("http://www.twitter.com")
        urls.append("http://www.yahoo.com")

        return urls[random.randrange(0,len(urls) - 1)]

def checkProxyFromList(ipcheck, *args):

	#	Check if you can connect to a
	#	proxy and request a website from
	#	it. Then write this to the working
	#	proxy list.

	global toCheck

        try:
                proxy_support = urllib2.ProxyHandler({"http":str(ipcheck)})
                opener = urllib2.build_opener(proxy_support) 
                urllib2.install_opener(opener) 
                urllib2.urlopen(str(getURLtoMakeRequest())).read() 

		#	We don't care about 404 / 300, etc. 
		#	Only successful connection
                n = file(savefile, "a+")
                n.write(ipcheck + "\n")
                n.close()

		#	We let the OS handle multiple
		#	writes to the same file by
		#	different threads.

        except:
                pass

	toCheck = toCheck - 1

def startThreadWithProxyToCheck(proxii):

	#	Start a new Python thread to check
	#	a proxy from the list inserted

	try:
                thread.start_new_thread(checkProxyFromList,(proxii,random.randrange(0,9000)))
        except:
                time.sleep(1)
                startThreadWithProxyToCheck(proxii)

if(len(sys.argv) != 3):
	proxyfile = raw_input("Enter the path of the proxies to check: ")
	savefile = raw_input("Enter the path to make the new proxy list: ")
else:
	try:
		proxyfile = sys.argv[1]
		savefile = sys.argv[2]
	except:
		print ("Usage: python proxyborder.py check-these.txt save-here.txt")
		exit(5)


try:
        h = file(savefile, "w+")
except:
        print "Could not open file to save working proxies."
        exit(1)

import fileinput
ProxiesToCheck = []
for line in fileinput.input([proxyfile]):
        ProxiesToCheck.append(string.replace(line, "\n", ""))

toCheck = len(ProxiesToCheck)

for px in ProxiesToCheck:
        startThreadWithProxyToCheck(px)


while(toCheck > 0):
	pass

