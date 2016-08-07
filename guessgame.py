import random
number = random.randint(1,100)
guess = 0
false = 0
while (guess == number) == false:
    guess = input("guess: ")
    if guess < number:
        print "too low"
    elif guess > number:
        print "too high"
print "you win"
