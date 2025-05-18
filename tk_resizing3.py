from tkinter import * 
import ttkbootstrap as tb 


root = tb.Window('darkly')
root.title("TTk Resizing")
root.geometry('400x200')


my_style = tb.Style()
my_style.configure("my.TButton",font = ("Helvetica",20))

my_label  = tb.Label(root, text="My label:",width=10,font = ("Helvetica",20))
my_label.pack(pady=20)

my_button = tb.Button(root, text="Click Me!",bootstyle = "success outline" ,width=10,style="my.TButton")
my_button.pack(pady=10)


root.mainloop()