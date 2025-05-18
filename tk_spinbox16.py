from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename = "vapor")
root.title("Ttk Spin box")
root.geometry("400x500")

def selector():
    my_label.config(text = my_spin.get())

my_value = ["ashish","nitin","vijay","dushyant"]

my_label = tb.Label(root, text = "My Spin Box",bootstyle = "info")
my_label.pack(pady=10)

my_spin = tb.Spinbox(root,values=my_value,bootstyle = "info",command = selector, state="readonly")
my_spin.pack()

root.mainloop()