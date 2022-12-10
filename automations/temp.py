#TEMP#
from arduino import pwr_to_pin, a_read
import time
temp=0
def run():
    global temp
    temp_pin = 0
    light_pin = 7
    temp=a_read(0,0)
    if (temp in range(15, 28)):
        pwr_to_pin(7,1,0)
    else:
        pwr_to_pin(7,0,0)
while (0==0):
    run()
    print(temp)
    time.sleep(10)