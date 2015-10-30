#!/usr/bin/python
time.strftime("%d/%m/%Y %H:%M:%S")
time.time(), #utc unix timestamp
#from python 3.3: use datetime.datetime.timestamp()
(datetime.datetime(2090,3,12) - datetime.datetime(1970,1,1)).total_seconds())
