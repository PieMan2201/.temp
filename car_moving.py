import time

car = "o-o"

moved = 0
move = 1

while True:
    if moved > 40:
        move = -1
    elif moved < 2:
        move = 1
    moved = move + moved
    print "\n" * 200
    print " " * moved, car


    time.sleep( 0.1)
