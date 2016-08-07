

man = """ |
/ \\"""

dance = 0
while 1:
    if dance == 0:
        left_arm = "\\"
        rightarm = "/"
    else:
        if dance == 1:
            left_arm = "-"
            rightarm = "-"
    if dance == 0:
        dance = 1
    else:
        if dance == 1:
            dance = 0
    for x in range(0,1000):
        print

    print " O "
    print left_arm + "|" + rightarm
    print man

    for x in range(0, 10*10*10*10*10*10):
        if x > 0:
            pass
        else:
            if x < 0:
                pass
        
