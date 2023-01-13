import tkinter as tk
import threading
import time

def button_code():
	print("sleeping for 10 seconds...")
	btn.lock()
	time.sleep(10)
	print("10 seconds done..!")
	btn.unlock()
	


def start():
	t1=threading.Thread(target=button_code)
	t1.start()

root = tk.Tk()
root.geometry("200x200+100+100")
btn=tk.Button(text="mybutton",command=start)
btn.pack(pady=30)

root.mainloop()
