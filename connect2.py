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
def handsfounction(hand):
    sentdata(10+hand, 1)
    # You need to see when the founction group is a start for your hand.
    # 10 is just a temp
def QrCodeFounction(Code):
    sentdata(-1+Code, 1)
def ColorFounction(code):
    sentdata(2+code, 1)
