#uncomment the lines below .
import time

def amClock(hours,mins,sec):
    print(hours  , ":" , mins , ":" , sec , "AM")
    return

def pmClock(hours,mins,sec):
    print(hours  , ":" , mins , ":" , sec , "PM")
    return

h = 0
m = 0
s = 0

while True:
    for i1 in range(1,48373) :

        s += 1
        # time.sleep(1)
        # un comment the line that is above this line if you want the clock to move in real life time  .


        if s == 61 :
            m += 1

        if m == 61:
            h += 1



        if m == 61 :
            m = 0

        if s == 61 :
            s = 0

        if h == 13 :
            h = 0

        amClock(h, m, s)


    for i in range(1,48374):
        s += 1
        # time.sleep(1)
        # un comment the line that is above this line if you want the clock to move in real life time  .

        if s == 61 :
            m += 1

        if m == 61:
            h += 1



        if m == 61 :
            m = 0

        if s == 61 :
            s = 0

        if h == 13 :
            h = 0

        pmClock(h,m,s)

