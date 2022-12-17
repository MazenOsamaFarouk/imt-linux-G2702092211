# SevenSegment module
import RPi.GPIO as gpio
COM_CATHODE=1
COM_ANODE=2

# 0b dot gfedcba
# common Cathode 
# SSD: Seven Segment Display
numbers=[
0b00111111,
0b00000110,
0b01011011,
0b01001111
]


Type=COM_CATHODE

pins=list()

"""
function to initialize GPIO pins used in driving th seven segment
"""
def Init(pins_list , SSD_Type ):
    gpio.setmode(gpio.BCM)
    
    # input validation
    global  pins
    global  Type
    if Type in [COM_ANODE,COM_CATHODE]:
        Type = SSD_Type
    else:
        print("initialization failed: Type should be either COM_ANODE or COM_CATHODE")
        return
    
    if len(pins_list) == 8:
        pins=pins_list.copy()
    else:
        print("initialization failed: pins list should be  8 pins")
        return
        
    for pin in  pins:
        gpio.setup(pin, gpio.OUT)


  
"""
function used to display the given number on seven segment
"""
def Display(num):
    global pins
    global Type
    global numbers
    SSD_num=numbers[num]
    for bn,pin in enumerate(pins):
        pinvalue=((SSD_num>>bn)&1)
        
        if Type==COM_CATHODE:
            if pinvalue==1:
                gpio.output(pin,gpio.HIGH)
            else:
                gpio.output(pin,gpio.LOW)
        else:
            if pinvalue==1:
                gpio.output(pin,gpio.LOW)
            else:
                gpio.output(pin,gpio.HIGH)
            
            
            
            
            
            
            
            
            
            
            