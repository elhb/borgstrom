#! /usr/bin/env python2.7

from borgstrom.session2 import *
import sys

#@profile
def solve():
	url = 'http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
	data = getServerData(url)
	reasons = getReasons(data)
	print getFraction(reasons,'REPAIR')
