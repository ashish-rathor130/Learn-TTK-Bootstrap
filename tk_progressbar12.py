from tkinter import * 
import ttkbootstrap as tb 
import time


root = tb.Window('vapor')
root.title("TTk Resizing")
root.geometry('400x200')

def increment():
    # my_pb.step(10)
    if my_pb["value"] <=100:
        my_pb["value"] +=10
    else:
        my_pb["value"]=0
    my_label.config(text = my_pb["value"])

def start():
    my_pb.start(10)
def stop():
    my_pb.stop()
def auto():
    if my_pb["value"] <=100:
        my_pb["value"] +=10
    else:
        my_pb["value"]=0
    my_label.config(text = my_pb["value"])
    root.update_idletasks()
    time.sleep(1)

my_label = tb.Label(root,text = "My Progress Bar",bootstyle = "warning")
my_label.pack(pady=10)

var1 = IntVar()
my_pb = tb.Progressbar(root,value=0, maximum=100, orient="horizontal", mode = "determinate",length=200,bootstyle = "danger")
my_pb.pack(pady=20)

btn_frame = tb.Frame(root)
btn_frame.pack(pady=20)

my_button = tb.Button(btn_frame, text = "Click Me!",bootstyle = "warning outline",command = increment)
my_button.grid(padx=5, pady=5,row = 0, column=0)
my_button = tb.Button(btn_frame, text = "Start!",bootstyle = "warning outline",command = start)
my_button.grid(padx=5, pady=5,row = 0, column=1)
my_button = tb.Button(btn_frame, text = "Stop!",bootstyle = "warning outline",command = stop)
my_button.grid(padx=5, pady=5,row = 0, column=2)
my_button = tb.Button(btn_frame, text = "Auto!",bootstyle = "warning outline",command = auto)
my_button.grid(padx=5, pady=5,row = 0, column=3)


root.mainloop()