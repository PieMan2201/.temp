number_to_see_if_prime = int(float(str(raw_input("ENTER A NUMBER: "))))
num = number_to_see_if_prime

if num == 0:
    print "weird number!"
elif num == 1:
    print "weird number!"
elif num == 2:
    print "prime"
else:
    number_isprime = False
    for checking_num in range(2,num):
        if int(num / checking_num) == float(str(float(num) / float(checking_num))):
            print "not prime"
            number_isprime = True
            break
    if number_isprime == False:
        print "prime"

