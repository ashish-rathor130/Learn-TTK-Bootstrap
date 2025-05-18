from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x350")
def selecter():
    my_label.config(text=f"you selected: {my_dentry.entry.get()}")
def qdate():
    cd = Querybox()
    my_label1.config(text = f"You selected : {cd.get_date()}")

my_label = tb.Label(root,text="Select Date",bootstyle="light")
my_label.pack(pady=10)

my_dentry = tb.DateEntry(root,bootstyle="light",startdate=date(day = 29,month=4,year=2025))
my_dentry.pack(pady=10)

my_btn = tb.Button(root,text="Click Me!",bootstyle = "warning outline",command=selecter)
my_btn.pack(pady=10)

# method 2

my_label1 = tb.Label(root,text="Select Date",bootstyle="light")
my_label1.pack(pady=10)

my_btn = tb.Button(root,text="Select Date!",bootstyle = "warning outline",command=qdate)
my_btn.pack(pady=10)


root.mainloop()