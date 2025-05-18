from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x250")

def start():
    my_fgage.start()
def auto():
    my_fgage.step(10)
    my_label.config(text = f"Position: {my_fgage.variable.get()}%")

def stop():
    my_fgage.stop()
    


my_label = tb.Label(root,text="Enter Text",bootstyle="light")
my_label.pack(pady=10)

my_fgage = tb.Floodgauge(root,text="my gauge",bootstyle="info", mask = "pos: {}%",orient="horizontal",value=10, maximum=100,mode="determinate",)
my_fgage.pack(pady=20,fill="x",padx=20)

btn_frame = tb.Frame(root)
btn_frame.pack(pady=10,padx=10)

my_btn = tb.Button(btn_frame,text="Start !",bootstyle = "warning outline",command=start)
my_btn.grid(row=0,column=0,padx=5)
my_btn = tb.Button(btn_frame,text="Incre !",bootstyle = "warning outline",command=auto)
my_btn.grid(row=0,column=1,padx=5)
my_btn = tb.Button(btn_frame,text="End !",bootstyle = "warning outline",command=stop)
my_btn.grid(row=0,column=3,padx=5)

root.mainloop()