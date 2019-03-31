# For this example I used the lecture notes and the article listed
# https://matplotlib.org/users/pyplot_tutorial.html

# Import the relevent libraries as plt to reduce the code
import matplotlib.pyplot as plt

# This is the question asked to the user
text = "Please Select from the following functions to plot 0-4 \n(A) X \n(B) X ^ 2 \n(C) 2^X\n(D) All graphs together!"
print(text)
ans = input("Option A, B, C, D:")

# Now we declare the variables for each of the graphs
x = []
x2 = []
twox = []

# Populate the above variables based on the range stated in the question
for i in range(0,5):
    x.append(i)
    x2.append(i**2)
    twox.append(2**i)

# This function will be used later in all examples to prevent re-writing code over and over
# This code lables the graph with a title and labels the Axis and plots the graph
def launch_graph():
    plt.title('Question 10: x and f(x)')
    plt.axis([0, 5, 0, 20])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

# The below function takes the selection from the user and plots the relevant one using the variables already defined
def plot(number):
    if number == "A":
        plt.plot(x,x,'r--')
        launch_graph()
    elif number == "B":
        plt.plot(x,x2,'bs')
        launch_graph()
    elif number == "C":
        plt.plot(x,twox,'g^')
        launch_graph()
    elif number == "D":
        plt.plot(x,x,'r--',x,x2,'bs',x,twox,'g^')
        launch_graph()
    else:
        print('Please select from one of the options!')

plot(ans)

