## In this instance I have used the following link to help me in this question.
## https://www.programiz.com/python-programming/examples/prime-number
## I have adapted it to read the way I would want it.
## The core of this question is how to calculate a prime number & having reviewed the above link it is clear - something that is divisible by only itself and one!

value = int(input("Please enter a positive integer: "))
# as previous questions the try element is to determine whether the user inputted a positive integer

try : 
   number = int(value)
   if number > 1:
       for i in range(2,number): ## for i in range 2,3,4,5,6....number - up to but not including number 
           if (number%i)==0:    ## we then divide our number chosen by the above range, loop through number/2../3../4 and so on up to number/(number-1), If any of these are true we have a number that divides into our chosen number
                                ## And this cant be the case! A zero remainder would mean it evenly devides 
               print(number, " is not a prime number!")
               break
       else:
            print(number, " is a prime number!")

except ValueError:
    print("This is not a integer!")