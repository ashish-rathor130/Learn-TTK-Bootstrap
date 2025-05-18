from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x250")

def get_data():
    data= my_entry.get()
    my_label.config(text = f"You Entered: {data}")

my_label = tb.Label(root,text="Enter Text",bootstyle="light")
my_label.pack(pady=10)

my_entry = tb.Entry(root,bootstyle="light" , font= ("Helvetica",10))
my_entry.pack(pady=10)

my_btn = tb.Button(root,text="Click Me!",bootstyle = "warning outline",command=get_data)
my_btn.pack(pady=10)

root.mainloop()