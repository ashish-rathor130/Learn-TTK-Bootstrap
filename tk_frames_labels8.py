from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename = "vapor")
root.title("Label and Frames")
root.geometry("500x600")

my_frame = tb.Frame(root, height=600)
my_frame.pack(fill="x", padx=20,pady=20)

my_label =tb.Label(my_frame, text = "This is my First Label", bootstyle = "")
my_label.pack(pady=5)


my_frame1 = tb.Frame(root, height=600,bootstyle = "primary", name = "screen frame")
my_frame1.pack(fill="x", padx=20,pady=10)

my_title = tb.Label(my_frame1,text = "Text Transformation",bootstyle = "light")
my_title.pack()

my_frames1 = tb.Frame(my_frame1, height=100,bootstyle = "light")
my_frames1.pack(fill="x", padx=20,pady=10)

my_text = Text(my_frames1,height=2)
my_text.pack(fill="both", pady=2, padx=2)

my_btn1 = tb.Frame(my_frame1)
my_btn1.pack(fill="x", padx=20,pady=10)

btn = tb.Button(my_btn1,text = "Click Me!",bootstyle ="warning outline")
btn.grid(row = 0,column=0,pady=5, padx=5)

btn = tb.Button(my_btn1,text = "Click Me!",bootstyle ="warning outline")
btn.grid(row = 0,column=1,pady=5, padx=5)

btn = tb.Button(my_btn1,text = "Click Me!",bootstyle ="warning outline")
btn.grid(row = 0,column=2,pady=5, padx=5)

btn = tb.Button(my_btn1,text = "Click Me!",bootstyle ="warning outline")
btn.grid(row = 0,column=3,pady=5, padx=5)



root.mainloop()