import time
from pyb import LED
import sensor
import connect2,function2
def sensorinit(sensor,mode):
    if mode == "templateMatch":
        sensor.set_contrast(1)
        sensor.set_gainceiling(16)
        # Max resolution for template matching with SEARCH_EX is QQVGA
        sensor.set_framesize(sensor.QQVGA)
        # You can set windowing to reduce the search image.
        #sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
        sensor.set_pixformat(sensor.GRAYSCALE)
    if mode == "QRCode":
        sensor.set_pixformat(sensor.RGB565)
        sensor.set_framesize(sensor.QQVGA)
        sensor.skip_frames(30)
        sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
    if mode == "Color":
        sensor.set_pixformat(sensor.RGB565)
        #设置图像色彩格式，有RGB565色彩图和GRAYSCALE灰度图两种
        sensor.set_framesize(sensor.QQVGA)  # 使用QQVGA的速度。
        #设置图像像素大小
        sensor.skip_frames(10)  # 让新的设置生效。
        sensor.set_auto_whitebal(False)  # turn this off.
        #关闭白平衡。白平衡是默认开启的，在颜色识别中，需要关闭白平衡。
def functionLED():
    red_led   = LED(1)
    green_led = LED(2)
    blue_led  = LED(3)
    ir_led	= LED(4)

    def led_control(x):
        if   (x&1)==0: red_led.off()
        elif (x&1)==1: red_led.on()
        if   (x&2)==0: green_led.off()
        elif (x&2)==2: green_led.on()
        if   (x&4)==0: blue_led.off()
        elif (x&4)==4: blue_led.on()
        if   (x&8)==0: ir_led.off()
        elif (x&8)==8: ir_led.on()
    for i in range(16):
        led_control(i)
        time.sleep(500)
def hand():
    sensor.rest()
    sensorinit(sensor,"templateMatch")
    function2.templateMatch(sensor, "hand")
def templatematchtest():
    sensor.reset()
    sensorinit(sensor,"templateMatch")
    sensor.set_pixformat(sensor.GRAYSCALE)
    function2.templateMatch(sensor, "233")
def QRCode():
    sensor.reset()
    sensorinit(sensor,"QRCode")
    code = 0
    while (code <3):
        code = function2.QrCodeScan(sensor)
        print(code)
        connect2.QrCodeFounction(code)
        time.sleep(3500)
def color():
    sensor.reset()
    sensorinit(sensor,"Color")
    back = 0
    while(back<4):
        back = function2.ColorMatch(sensor)
        print(back)
        connect2.ColorFounction(back)
        time.sleep(4000)
def main():
    color()
    templatematchtest()
    QRCode()
if __name__ == '__main__':
    main()
