#!/usr/bin/python


import threading
import time

exitFlag = 0


class WebCrawlerTrhread(threading.Thread):
    def __init__(self, threadID, list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.list = list

    def run(self):
        print "Starting", self.threadID
        for l in self.list:
            print l
        print "Exiting", self.threadID
