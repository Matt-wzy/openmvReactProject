import time
from pyb import UART
def sentdata(FounctionGroup,times):
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

def sendnumberchange(number, mode):
    if mode == 1:
        pass
    elif mode == 2:
        return (hex(number))
    elif mode == 3:
        return (chr(int(number)))

def sendnumber(number, times,mode):
    '''
    Important reminding:
        you need to give me the 10 int number to send, but the 0xff is still useful.
        In a word , you need to press 0xff to make it work.
    '''
    print("Connection succeed", number)
    uart = UART(3, 115200)
    buf = sendnumberchange(number, 3)
    while(times):
        uart.write(buf)
        times -= 1
