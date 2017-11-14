#!/usr/bin/python

import memcache
client=memcache.Client([('127.0.0.1',11211)])
for i in range(500):
	client.incr("counter")
	cn=client.get("counter")
        client.set(cn,"new value")
        client.get(cn)
