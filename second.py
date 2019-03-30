# https://youtu.be/e32vab7cGdM
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# I used two sources to complete this problem
# Before starting i was unaware of how each line was refered to when dealing with text file. 
# The formula for outputting every second line was straight forward a for statement with a nested if statment in it.
# Once i watched the attached video the argement was clear
import sys

fileSelect = sys.argv[1]

file = open(fileSelect, "r")
linenum = 0

for line in file:
    linenum += 1
    if linenum % 2 == 0:
        print(linenum)
