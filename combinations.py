import random
def gn():
    return random.randint(0,9)
x = 0
while x < 500000:
    print "\r" + str(gn()),
    x += 1
x = 0
while x < 400000:
    print "\r1" + str(gn()),
    x += 1
x = 0
while x < 300000:
    print "\r13" + str(gn()),
    x += 1
x = 0
while x < 200000:
    print "\r133" + str(gn()),
    x += 1
print "\r1337"

