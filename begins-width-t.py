import time
from datetime import datetime

date = datetime.now()

day = date.strftime("%A")

daylet = day[0]

if daylet == "T":
    print ("Today begins with the letter T:" + day)
else:
    print ("Today " + day + " dose not start with the letter T")
