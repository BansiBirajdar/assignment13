import urllib.request as urllib2

def is_connected():
    try:
        urllib2.urlopen("http://google.com",timeout=1)
        return True
    except urllib2.URLError as e:
        return False