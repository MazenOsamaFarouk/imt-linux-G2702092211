# push button test
import RPi.GPIO as gpio
import time
import tkinter as tk

DEBOUNCE_TIME=50/1000
btn_pin=4
btn_val=0

led_pin=5
# XOR ->  '^'
# 1 ^ 0 -> 1
# 1 ^ 1 -> 0 
# 1 ^ x -> ~x
ledstatus=0

number=0


def ToggleLed():
    global ledstatus
    global number
    ledstatus=ledstatus^1
    gpio.output(led_pin, ledstatus)
    number+=1
    number_label.config(text=str(number))




def CheckButton(pinNumber):
    btn_val=gpio.input(btn_pin)
    if(btn_val == 0): # because Pull UP
        time.sleep(DEBOUNCE_TIME)
        btn_val=gpio.input(btn_pin)
        if(btn_val == 0):
        # That means the state of button is pressed.
              ToggleLed() 
    
    # TODO: Re-schedule reading of button again
    #main.after(1,CheckButton)
    
# recap funcitons in C: 
# prototype/signature: void function(int a, int b);

# void function(int a);
gpio.setmode(gpio.BCM)
gpio.setup(btn_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.add_event_detect(btn_pin,gpio.FALLING,callback=ToggleLed, bouncetime=DEBOUNCE_TIME*1000)

gpio.setup(led_pin,gpio.OUT)



# init Tkinter GUI
main = tk.Tk()
main.geometry("200x200+20+20")
main.title("pi tkinter toggle led with push button")

number_label = tk.Label(main,text=str(number))
number_label.pack(padx=30,pady=30)

# No checking in while loop becasue its now based on interrupt
#main.after(1,CheckButton)
main.mainloop()
    










