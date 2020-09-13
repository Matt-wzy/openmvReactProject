import function2
import sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)  # can be QVGA on M7...
sensor.skip_frames(30)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
code = function2.QrCodeScan(sensor)
print(code)
