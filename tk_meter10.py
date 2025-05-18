from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename = "vapor")
root.title("TTk Menubutton")
root.geometry("500x600")

counter = 10
def increaser():
    global counter
    if counter <= 100:
        my_meter.configure(amountused = counter)
    counter +=10

    my_btn.configure(text = my_meter.amountusedvar.get())

def up():
    my_meter.step(10)
def down():
    my_meter.step(-10)




my_meter = tb.Meter(root,bootstyle="info",amountused=0,amounttotal=100,metersize=200,showtext=True,subtext="Learned TTk",interactive=True,textleft="$",textright="%",meterthickness=10,metertype="full",subtextstyle='light')
my_meter.pack(padx=10,pady=20)


btn_frame = tb.Button(root)
btn_frame.pack(pady=5,padx=5)

my_btn = tb.Button(btn_frame,text = "click me!",command=increaser,bootstyle = "info outline")
my_btn.grid(row = 0, column = 0,padx=2,pady=2)

my_btn = tb.Button(btn_frame,text = "Down !",command=down,bootstyle = "info outline")
my_btn.grid(row = 0, column = 1,padx=2,pady=2)

my_btn = tb.Button(btn_frame,text = "Up !",command=up,bootstyle = "info outline")
my_btn.grid(row = 0, column = 2,padx=2,pady=2)

root.mainloop()