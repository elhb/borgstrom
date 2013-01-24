#! /usr/bin/env python2.7

from borgstrom import *

url = 'http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
data = getServerData(url)
reasons = getReasons(data)
print getFraction(reasons,'REPAIR')