# mazenofarouk.pythonanywhere.com
import RPi.GPIO as gpio
import requests
import time

led_pin = 2



gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)


while True:
    data=requests.get("http://mazenofarouk.pythonanywhere.com/")
#    if str(data.text) == "b'ON'":
    if "ON" in str(data.text):
        gpio.output(led_pin, gpio.HIGH)
    elif "off" in str(data.text):
        gpio.output(led_pin, gpio.LOW)
    else:
        print("Invalid response")
        
    time.sleep(0.5)