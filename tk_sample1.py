from tkinter import *
import ttkbootstrap as tb

# root window 
def click():
    out = my_entry.get()
    my_label.config(text = out)

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x250")


my_label = tb.Label(root,text="",bootstyle = "success")
my_label.pack(pady=10)

my_entry = tb.Entry(root, bootstyle ="warning")
my_entry.pack(pady=10)


btn_frames = tb.Frame(root,bootstyle = "")
btn_frames.pack(pady=20,padx = 20)

my_button = tb.Button(btn_frames, text = "Click Me!" ,bootstyle = "warning outline" , command = click)
my_button.grid(row=0,column=0, pady=10 ,padx = 5)

my_button = tb.Button(btn_frames, text = "Quite Me!" ,bootstyle = "danger outline" , command = root.destroy)
my_button.grid(row=0,column=1, pady=10,padx=5)

root.mainloop()