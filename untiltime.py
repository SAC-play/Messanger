from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=16, minute=34, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    ticks = time. time()
    print("Current ticks =", ticks)
    print("adios")

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('keep running\n\n\n\n\n')

t = Timer(secs, hello_world)
t.start()
t2 = Timer(secs, hello_world)
t2.start()
print ("olah!")



countdown(10)


