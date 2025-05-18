from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename ="vapor")
root.title("Ttk Scroll bar")
root.geometry("400x500")


my_frame = tb.Frame(root)
my_frame.pack(pady=10)

my_label = tb.Label(root, text = "My Scroll Bar",bootstyle  ="info",font = ("Helvetica",18))
my_label.pack(pady=20)

my_scrollbar = tb.Scrollbar(my_frame, bootstyle = "round info",orient= "vertical")
my_scrollbar.pack(fill="y",side="right")

my_text = tb.Text(my_frame,yscrollcommand=my_scrollbar.set,wrap="none",font= ("Helvetica",18), height=6,)
my_text.pack(padx=10)

my_scrollbar.config(command=my_text.yview)


my_btn = tb.Button(root,text = "Click Me!", bootstyle = "success outline round",)
my_btn.pack(pady=20)

root.mainloop()