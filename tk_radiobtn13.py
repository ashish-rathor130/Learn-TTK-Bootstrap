from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x350")

def clicker():
    my_label.config(text=f"you selected {var1.get()}")


my_label = tb.Label(root, text="RadioBTN")
my_label.pack(pady=20)

my_topping = ["mango","papaya","orange","guava"]

var1 = StringVar()
for topping in my_topping:
    tb.Radiobutton(root, variable=var1, text=topping,bootstyle = "danger", value=topping).pack()


my_btn = tb.Button(root, text ="Click Me!",bootstyle = "success outline",command=clicker,)
my_btn.pack(pady=20)

my_rb = tb.Radiobutton(root, text="RadioBTN",value= "Radio Button1",bootstyle = "toolbutton info outline", variable=var1, command=clicker)
my_rb.pack(pady=20)

root.mainloop()