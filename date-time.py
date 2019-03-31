from datetime import datetime as dt
from datetime import date
# http://strftime.org/
# https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime

# Using the above website it was straightforward to manipulate the string to the desire format. 
# The issue i found was the "th" following the 10 - 
# 1st, 2nd, 3rd, 4th, 5th.....31st
# So if the number ends with 1 "st" is required, 2 "nd", 3 "rd" and everthing else requires a th

# List of all the date endings that is not "th" this was modified from the above stakoverflow page 
endings = {    
    1: 'st',
    2: 'nd',
    3: 'rd',
    21: 'st',
    22: 'nd',
    23: 'rd',
    31: 'st',
}

# The function to determine the date in the required format
def today():
    # Declare today
    moment = dt.today()

    # I couldnt find AM/PM in lower case therefore I made it 
    apm = moment.strftime('%p').lower()

    try:
        end = endings[moment.day]
    except KeyError:
        end = "th"   
    print(moment.strftime(f'%A, %B %d{end} %Y at %I:%M{apm}'))


today() # The function needs to be called at the end



