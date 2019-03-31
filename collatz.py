# The first problem with this question was to determine what the collatz series was.

# Ask the user to input an integer
value = input("Please enter a positive integer:")

# We have to determine whether the user did in fact input an integer using try and except
try : 
    number = int(value)
    while number > 1:
        if (number%2) == 0: # If the number is even the modulus remainder will be zero
            number = (number/2) # Divide by two
            print(number)
        else: # If the number is odd multiply by 3 and add 1
            number = (number*3)+1
            print(number)


except ValueError:
    print("This is not a integer!")