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