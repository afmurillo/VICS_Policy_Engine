import os
import sys
import urllib2

from threading import Thread

def make_request(name, id):
    os.popen("openstack network set --name field" + name + " " + id)

def main():
    name = sys.argv[1]
    number = int(sys.argv[2],10)
    for i in range(number):
	#id = "4ccd3c99-3869-423e-8130-06258bb4bd5"+str(i)
	#print id
        Thread(target=make_request, args=(name, "4ccd3c99-3869-423e-8130-06258bb4bd5"+str(i),)).start()

    id = "4ccd3c99-3869-423e-8130-06258bb4bd5f"
    Thread(target=make_request, args=(name, id,)).start()

main()

