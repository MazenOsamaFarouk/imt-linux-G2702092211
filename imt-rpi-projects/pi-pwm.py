# pi PWM with gpio
import RPi.GPIO as gpio
import time
import tkinter as tk


led_pin=2
pwmFreq=100


gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

pwmCh=gpio.PWM(led_pin, pwmFreq)
pwmCh.start(0)
# 20Hz -> 20KHz
# 150 -> 350
# pwmCh.ChangeFrequency()

"""
while True:
    # Fade in effect
    for duty in range(1,100,5):
        pwmCh.ChangeDutyCycle(duty)
        time.sleep(0.25)
    # Fade out effect   
    for duty in range(100,1,-5):
        pwmCh.ChangeDutyCycle(duty)
        time.sleep(0.25)
"""

def ChangePWM(SliderVal):
    
    pwmCh.ChangeDutyCycle(Duty.get())


# init Tkinter GUI
main = tk.Tk()
main.geometry("200x200+20+20")
main.title("pi tkinter toggle led")

Duty=tk.IntVar()
Slider = tk.Scale(main,label="Duty", orient=tk.HORIZONTAL,variable=Duty, command=ChangePWM,from_=5,to=10,resolution=1/18 )

Slider.pack(pady=50, padx=20)

main.mainloop()
