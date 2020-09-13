import sensor, image, time
import connect2
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
connect2.sentdata(6,1)
print("Connection succeed")
time.sleep(2000)
#while(True):
	#clock.tick()
	#img = sensor.snapshot()
	#print(clock.fps())