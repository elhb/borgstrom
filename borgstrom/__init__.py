#

def main():
    pass
    
def getServerData(url):
    """get the file from the url and returns it in one chunk
    """
    from urllib2 import urlopen
    data = urlopen(url).read()
    return data

def getReasons(data):
    """ get reasons for outages from XML file formatted like http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml,
    see more info at http://www.grandcentral.org/developers/download.html
    returns list of reasons one for each outage.
    """
    import untangle
    data = untangle.parse(data)
    outages = data.NYCOutages.outage
    reasons = []
    for outage in outages:
        reasons.append(outage.reason.cdata)
    return reasons

def getFraction(reasons,reason):
    """ counts the number of occurances of reason in reasons and returns the fraction in format 'count'/'total'.
    """
    return str(reasons.count(reason))+'/'+str(len(reasons))

if __name__ == "__main__":
    main()

