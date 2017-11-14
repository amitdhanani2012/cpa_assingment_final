#!/usr/bin/python

import memcache
client=memcache.Client([('127.0.0.1',11211)])
client.set("counter","10")
