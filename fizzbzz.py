for x in range(1, 101):
    if x % 3 == 0:
        print "fizz",
    if x % 5 == 0:
        print "buzz",
    if x % 3 != 0 and x % 5 != 0:
        print x,
    print
