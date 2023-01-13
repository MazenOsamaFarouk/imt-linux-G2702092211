

import serial

PORT="/dev/serial0"
BAUD=115200


uart=serial.Serial(PORT,BAUD)


if uart.isOpen():
	print("uart device opened successfully")
	
	# byte array char[]
	uart.write("Hello from pyserial!!\r\n".encode())
	
	while True:
		line = uart.readline() # returns a byte array
		if line.decode() != "":
			print("Recieved line:" + line.decode() + "from Rpi")



