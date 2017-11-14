#!/usr/bin/python

import memcache
client=memcache.Client([('127.0.0.1',11211)])
print "counter value is %s " % client.get("counter")
