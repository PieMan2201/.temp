import time
import urllib

start = time.time()

try:
    urllib.urlopen("http://google.com")
except:
    print "you have no internet!"
timed = time.time() - start

if timed < 0.5:
    print "your wifi is very string!"
elif timed < 2:
    print "your wwfi is okay"
else:
    print "your wifi is weak!"
