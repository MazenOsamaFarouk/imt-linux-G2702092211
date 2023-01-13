from threading import Timer
import threading
# import time
import RPi.GPIO as gpio

# Excersise:
# use threads to create an application that toggles
# led1 -> 500 ms
# led2 -> 1000 ms
# should be blinking at the same time (concurrent)


led_pin1=2
led_pin2=3
toggle1=0
toggle2=0

def led1():
	gpio.output(led_pin1, toggle1)
	toggle1=toggle1^1
	# time.sleep(0.5)
	timer_led1=Timer(0.5,led1)
	timer_led1.start()
	
def led2():
	gpio.output(led_pin2, toggle2)
	toggle2=toggle2^1
	# time.sleep(1)
	timer_led2=Timer(1,led2)
	timer_led2.start()
	
	
gpio.setmode(gpio.BCM)
gpio.setup(led_pin1, gpio.OUT)
gpio.setup(led_pin2, gpio.OUT)

# th_led1=threading.Thread(target=led1)
# th_led2=threading.Thread(target=led2)

# th_led1.start()
# th_led2.start()

timer_led1=Timer(0.25,led1)
timer_led2=Timer(2,led2)


timer_led1.start()
timer_led2.start()

while True:
	pass



