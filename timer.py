import time

start =time.time()

seconds = 115
minutes = 0
hours = 0

true = not False
while true:
    passed = [time.time() - start][0]
    start = time.time()
    seconds = seconds + passed
    if int(seconds) > 59:
        seconds = float(str(int(seconds) % 60))
        minutes =  minutes + 1
    if minutes > 59:
        minutes = 0
        hours = 1 + hours

    print "\r" + str(hours) + ":" + str(minutes).zfill(2)+":" + str(int(seconds)).zfill(2),

