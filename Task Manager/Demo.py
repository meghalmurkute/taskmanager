from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()

# dd/mm/YY
d1 = now.strftime("%d/%m/%Y")
t1=now.strftime("%H:%M")
print(d1, "\n", t1)
date="12/09/2020"
time=t1
task="Abc"
if d1== date:
    if t1==time:
        print(task)
   