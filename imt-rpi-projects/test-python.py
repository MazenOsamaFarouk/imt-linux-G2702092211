import RPi.GPIO as GPIO
import time as t

led_pin=2

# print("Hello World")
GPIO.setmode(GPIO.BCM)

# GPIO modes: GPIO.IN , GPIO.OUT
# GPIO Output Vlaues: GPIO.HIGH, GPIO.LOW
GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,GPIO.HIGH)

while True:
    
    GPIO.output(led_pin, GPIO.HIGH)
    t.sleep(0.5)
    GPIO.output(led_pin, GPIO.LOW)
    t.sleep(0.5)
