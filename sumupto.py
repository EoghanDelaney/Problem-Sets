#First attempt at problem one

#First thoughts on this problem are user input, positive interage and output the sum of numbers between it and that number.
#First how to ask the user to input something
#Secondly use an if statement to see if the value entered is a in fact a positive interage
#Then calculate out the formula and output the answer

#value = input("Please enter a positive integer:")

#if value > 0:
#    print("is a number!")
#    print(value)
#else:
#    print("NOT A NUMBER")
#    print(value)

#The above is my first attempt and my thinking was to build it up. Firstly when my input read out correctly i could move forward to the the formula with a nested if statement
# I then adapted the below "try except" from the attached website based on the errors i was getting "ValueError" :https://pynative.com/python-check-user-input-is-number-or-string/

value = input("Please enter a positive integer:")
try : 
    number = int(value)
    if (number > 0):
        x=0
        for i in range(number):
            x += (i+1)
        print(x)
    else:
        print("This is less than 0 - Therefor not positive!")
except ValueError:
    print("This is not a integer!")


# My Explanation
# I have Declared value as my input variable and asked for "please enter a..."
#I have then used a Try expect function as mentioned above try one thing and if there is an error print the following "This is not..."
#The try element is where the calculation is worked out if the input is greater than 0 we can continue.
# I then declared a term X this can hold the sum value. I then used the range from Zero to the number to add to X
# 