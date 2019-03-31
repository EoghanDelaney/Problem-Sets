# This problem was relatively straightforward 
# We look through the range from 1000 to 10,000
# First parameter we divide i by 6 and if the remainder is zero, therefore it is divisible 
# by 6, we proceed to the second step, if the remainder once i is divided by 12 is not equal 0 
# we can print i

for i in range(1000,10000):
    if i%6 == 0:
        if i%12 != 0:
            print(i)
        else:
            pass
    else:
        pass