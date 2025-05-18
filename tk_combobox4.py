from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='vapor')
root.title("TTk Combo Box")
root.geometry("400x600")

def get_value():
    value = my_cbox.get()
    my_label.config(text = f"You selected - {value}")

def click_bind(vl):
    value = my_cbox.get()
    my_label.config(text = f"You selected - {value}")
    

my_label = tb.Label(root,text="",bootstyle= "info")
my_label.pack(pady=20)

# dropdown values
values = ["Ashish","Nitin","Vijay","Dushyant"]

my_cbox = tb.Combobox(root,bootstyle= "info",values=values)
my_cbox.pack(pady=20)

# set default value
my_cbox.current(0)

#bind cbox
my_cbox.bind("<<ComboboxSelected>>", click_bind)

my_btn = tb.Button(root,text = "Click Me!",bootstyle= "info",command=get_value)
my_btn.pack(pady=20)

root.mainloop()