print 0
print 1
print 1
one = 1
two = 1
x = 0
while True:
    if x > 10:
        break
    new = one + two
    print new
    one = two
    two = new
    x += 1
