import matplotlib.pyplot as plt


text = "Please Select from the following functions to plot 0-4 \n(A) X \n(B) X ^ 2 \n(C) 2^X\n(D) All graphs together!"
print(text)
ans = input("Option A, B, C, D:")
x = []
x2 = []
twox = []

for i in range(0,5):
    x.append(i)
    x2.append(i**2)
    twox.append(2**i)

def launch_graph():
    plt.title('Question 10: x and f(x)')
    plt.axis([0, 5, 0, 20])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

#print(x, x2, twox)

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

