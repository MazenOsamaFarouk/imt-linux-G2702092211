import threading
import time
from threading import Lock # Mutex: Mutual Exclusion



# FIFO: queue
# shared resource
x=0

def increment_x():
	global x
	x += 1



def thread1(lock):
	# print("Hi from Thread 1 ")
	# time.sleep(1)
	for _ in range(100000):
		# lock usage of x
		lock.acquire()
		increment_x()
		# release lock of x
		lock.release()
		

def thread2(lock):
	# print("Hello from Thread 2")
	# time.sleep(1)
	for _ in range(100000):
		# lock usage of x
		lock.acquire()
		increment_x()
		# release lock of x
		lock.release()
	

# concurrent programming
mutex=Lock()
t1 = threading.Thread(target=thread1, args=(mutex,))
t2 = threading.Thread(target=thread2, args=(mutex,))



print("value of x is {0}".format(x))










t1.start()
t2.start()


# join: waits for a thread to finish execution
t1.join()
t2.join()

print("value of x is {0}".format(x))

