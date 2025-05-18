from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename = "superhero")
root.title("TTk Checked Boxes")
root.geometry('400x500')

def checked():
    if var1.get() == 1:
        my_label.config(text = "Box is checked",bootstyle  = "info")
    else:
        my_label.config(text = "Box is not checked" ,bootstyle  = "info")

def rchecked():
    if var2.get() == 1:
        my_label.config(text = "Round-Togg is checked",bootstyle  = "primary")
    else:
        my_label.config(text = "Round-Togg is not checked",bootstyle  = "primary")

def schecked():
    if var3.get() == 1:
        my_label.config(text = "Square-Togg is checked",bootstyle  = "success")
    else:
        my_label.config(text = "Square-Togg is not checked",bootstyle  = "success")


my_label = tb.Label(root, text = "My Checked: ",bootstyle = "info")
my_label.pack(pady=20)

var1 = IntVar()
my_box1 = tb.Checkbutton(root,text = "Check Simple box!",variable=var1, offvalue=0, onvalue=1,bootstyle = "info",command=checked)
my_box1.pack(pady=20)

var2 = IntVar()
my_box1 = tb.Checkbutton(root,text = "Check Round Toggle",variable=var2, offvalue=0, onvalue=1,bootstyle = "primary round-toggle",command=rchecked)
my_box1.pack(pady=20)

var3 = IntVar()
my_box1 = tb.Checkbutton(root,text = "Check Square Toggle",variable=var3, offvalue=0, onvalue=1,bootstyle = "success square-toggle",command=schecked)
my_box1.pack(pady=20)

my_btn = tb.Button(root, text="Quit!",bootstyle = "danger outline", command = root.destroy)
my_btn.pack(pady=20)

root.mainloop()