import tkinter as tk
import RPi.GPIO as gpio

led_pin=4
led_status=0

def toggle_led():
    global led_status
    if led_status==1:
        gpio.output(led_pin, gpio.HIGH)
        led_status=0
    elif led_status==0:
        gpio.output(led_pin, gpio.LOW)
        led_status=1

# init GPIO
gpio.setmode(gpio.BCM)
gpio.setup(led_pin,gpio.OUT)

# init Tkinter GUI
main = tk.Tk()
main.geometry("200x200+20+20")
main.title("pi tkinter toggle led")
led_btn = tk.Button(main, text="Toggle Led", command=toggle_led)

led_btn.pack(pady=20)

main.mainloop()