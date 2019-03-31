# This problem was straightforward - firstly asking the user to input a positive number 
# THen we must insure it is a number using the try except
# Once confirmed we apply an if statement if thr number is greater or equal to 1
# number to the power of a half is the same as the square root
# This is the printed out on the command line
import math
number = input("Please enter a positive number:")

def sqr(value):
    try : 
        number = float(value)
        if number >=1:
            sqrt = number**(0.5)
            print("The square root of " + str(number) + " is approx. " + str(round(sqrt,1)))
        else:
            print("")

    except ValueError:
        print("This is not a positive number!")

sqr(number)