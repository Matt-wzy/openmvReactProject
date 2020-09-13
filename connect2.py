import time
from pyb import UART
def sentdata(FounctionGroup,times):# If you need to send data, firstly change this place, useing sendnumber()function to send something like 0xff or some thing like this.
    print("Connection succeed",FounctionGroup)
    uart = UART(3, 115200)
    uart.write("#STOP\r")
    time.sleep(150)
    uart.write("#")
    uart.write(str(FounctionGroup))
    uart.write("GC")
    uart.write(str(times))
    uart.write("\r")
    UART.deinit()
def handsfounction(hand):
    sentdata(10+hand, 1)
    # You need to see when the founction group is a start for your hand.
    # 10 is just a temp
def QrCodeFounction(Code):
    sentdata(-1+Code, 1)
def ColorFounction(code):
    sentdata(2+code, 1)

def numberchange(number, mode):
    if mode == 1:
        return (int(number))
    elif mode == 2:
        return (hex(number))
    elif mode == 3:
        return (chr(int(number)))

def sendnumber(number, times,mode):
    '''
    Important reminding:
        you need to give me the 10 int number to send, but the 0xff is still useful.
        In a word , you need to press sendnumber(0xff, .. , ..) to make it work.
    '''
    print("Connection succeed", number)
    uart = UART(3, 115200) # You need to change this place so that you can use openmv for your team.
    buf = numberchange(number, mode) #I wrote three mode of sending the 0xff, I don't know which one is Ok for your bord, please try it to make it work.
    while(times):
        uart.write(buf)
        times -= 1
