import threading
import queue
import subprocess
from subprocess import Popen, PIPE
import queue
import time
from time import gmtime, strftime
import sqlite3 as db

ips = []
names = []

# open csv file that has site names and IP addresses.  Name should be names.csv and be in the same directory.
fhand = open("./names.csv")
# go through file and pull ip addresses into list ips.  Skip first row since it is the header.
# the header must be Name, GATEWAY
k = 0
for line in fhand:
    if k > 0:  # skip header
        ip = line.split(',')[1].strip()
        ips.append(ip)
        name = line.split(',')[0].strip()
        names.append(name)
    else:
        k += 1


class InsertionThread(threading.Thread):
    def __init__(self, dat):
        super(InsertionThread, self).__init__()
        self.name, self.ip = dat

    def run(self):
        name = self.name
        ip = self.ip
        vals = []
        # ping with Popen thread
        p1 = Popen(["ping", '-c 1', '-n', '-Q 184', '-W 1', ip], stdout=subp
