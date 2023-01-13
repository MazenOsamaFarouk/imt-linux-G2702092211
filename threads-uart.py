import serial
import threading
import queue
import time


def FillQueue(uart, q):
	while True:
		line = uart.readline()
		q.put(line.decode())
		


def ReadQueue(q):
	while True:
		time.sleep(3)
		print(q.get())
		


uart = serial.Serial("/dev/ttyS0",115200)
qu = queue.Queue()
t1 = threading.Thread(target=FillQueue, args=(uart,qu) )
t2 = threading.Thread(target=ReadQueue, args=(qu, ))

t1.start()
t2.start()

while True:
	pass
