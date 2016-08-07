import urllib

try:
    urllib.urlopen("http://www.google.com")
    print "success! you have Wifi internet."
except:
    print " you are not connected to the internet!"
