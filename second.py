# https://youtu.be/e32vab7cGdM
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# I used two sources to complete this problem
# Before starting I was unaware of how each line was referred to when dealing with text file. 
# The formula for outputting every second line was straightforward, a "for loop" statement with a nested "if statement" in it.
# Once I watched the attached video the argument was clear
import sys
fileSelect = sys.argv[1] # choose the file the second item in the list

file = open(fileSelect, "r") # open the fie as a read only
linenum = 0 # declare the line variable 0

for line in file:
    linenum += 1 # Add 1 to linenum
    if linenum % 2 == 0: 
        print(linenum)

# As mentioned above, the "for loop" loops through all the lines in the text file opened and if the line number has a remainder, 
# it will not be printed. Only the lines with a remainder of zero will be printed (every second line)