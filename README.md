# Problem Set Solutions Eoghan Delaney

This repository contains my solution to the Problem Set 2019 for the module Programing and Scripting at GMIT.

Having completed the problem set I believe I have a better grasp programming and of using python.

## How to download the repository
There are two ways to download/clone the repositories, One if you have GIT installed on your machine otherwise we can download a Zip file containing all the scripts.
When using GIT we follow the below steps
 - - Open your command line on your machine.
    - Move to a directory you wish to save the files into using the following commands cd followed by the file path eg *cd C:\Users\eoghan\Desktop\pands-problem-set*
    - Once in the directory you now clone the repository using the following command ***"git clone https://github.com/EoghanDelaney/Problem-Sets"***
    - The folder should now be in the directory listed in step B

If you do not have access to git the following steps can be taken.
 - - On you internet browser navigate to the following URL https://github.com/EoghanDelaney/Problem-Sets
    - Listed on the page is a green button **"Clone or download"** - click this button.
    - Once the dropdown appears click the **"Download Zip"** button. This will automaticly download the files to your downloads.
    - Navigate to your downloads folder on your computer and the folder will be visible.
    - The folder can now be cut/copied into a folder of your choose.
    - Finally you can now Unzip the folder by right-clicking on it and selecting unzip.



## How to run the code
Once the repository is downloaded the following steps are required to run the code.
- Please log on to anaconda.com and download the latest version of Python 3 (this comes with a number of moduels preinstalled that will come in helpful).
- Once complete we must now download all the most uptodate modules using ***pip***. As above we must open the command line and type the following command "**pip install moduleName**".
    - These are a list of the module names used in the problemset - ***time***, ***datetime***, ***matplotlib***, ***sys***, ***math*** - some of these may come as part of the Anaconda package and it will return *Requirement already satisfied*.
- In order to run each of the scripts we navigate to the download/saved location and write the following command "***python filename.py***". This will then execute the solution I have written.

## What each file contains
Below is a list of the soultions and question (The questions are transcribed directly from the question paper)

    1. **sumupto.py** - Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
    
    2. **begins-with-t.py** - Write a program that outputs whether or not today is a day that begins with the letter T. 
    
    3. **divisors.py** - Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
    
    4. **collatz.py** - Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
    
    5. **primes.py** - Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
    
    6. **secondstring.py** - Write a program that takes a user input string and outputs every second word.

    7. **squareroot.py** - Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

    8. **datetime.py** - Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.

    9. **second.py moby-dick.txt** - Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

    10. **pot-x.py** - Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4]



## References
I have used a number of sources to complete the problem sets. I have listed the modules and external references at the start of each of the problems.