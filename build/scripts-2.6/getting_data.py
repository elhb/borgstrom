#!/Users/erikborgstrom/.virtualenvs/py2.7/bin/python

from borgstrom.session2 import *

url = 'http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
data = getServerData(url)
reasons = getReasons(data)
print getFraction(reasons,'REPAIR')