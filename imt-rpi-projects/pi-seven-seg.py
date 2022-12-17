# seven segment driving using Rpi GPio
import tkinter as tk
import SevenSegment as SSD



# 0b dot gfedcba
SSD_pins=[ 2,3,4,5,6,7,8,9  ]
        #  0 1 2 3 4 5 6 7
SSD_number=0

def Increment():
    global SSD_number
    SSD_number = SSD_number +1
    SSD.Display(SSD_number%len(SSD.numbers))
    # n%m --> [0 ~ m-1]


# init GPIO

SSD.Init(SSD_pins,SSD.COM_CATHODE)
SSD.Display(0)

# init Tkinter GUI
main = tk.Tk()
main.geometry("200x200+20+20")
main.title("pi tkinter increment 7 segment")
led_btn = tk.Button(main, text="Increment", command=Increment)

led_btn.pack(pady=20)

main.mainloop()