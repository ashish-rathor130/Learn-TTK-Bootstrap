import ttkbootstrap as tb
from tkinter import *

root = tb.Window(themename = "vapor")
root.title("TTk Separator")
root.geometry("400x500")

my_label = tb.Label(root , text = "My Ttk Separator1",bootstyle = "info",font= ("Helvetica",15))
my_label.pack(pady=20)

my_sep = tb.Separator(root, takefocus=True, orient="horizontal",bootstyle ="info")
my_sep.pack(pady=10,fill="x",padx=20)

my_label1 = tb.Label(root , text = "My Ttk Separator2",bootstyle = "info",font= ("Helvetica",15))
my_label1.pack(pady=20)


my_grip = tb.Sizegrip(root,bootstyle = "info")
my_grip.pack(fill=X,side=BOTTOM,pady=5,padx=5,anchor="se")


root.mainloop()