# For this problem I used the python documentation http://strftime.org/
# Once datetime can determine the day of the week in string format the rest is straightforward

import time
from datetime import datetime

date = datetime.now() # using datetime get todays date

day = date.strftime("%A") # get the day of the week in text format "Thursday"

daylet = day[0] # get the first letter of the day

# Now a straightforward if statement to compare the output from daylet
if daylet == "T":
    print ("Yes - Today begins with the letter T:" + day)
else:
    print ("No - Today " + day + " dose not start with the letter T")


# The above was my original attempt, however upon completing the remainder of the questions 
# I believe the following is valid also for cleaner code 
# daylet = (datetime.now().strftime("%A"))[0] 

