import ttkbootstrap as tb 
from tkinter import * 
from ttkbootstrap.scrolled import ScrolledText


root = tb.Window(themename="vapor")
root.title("TTk Scrolled Text")
root.geometry("500x600")

my_label = tb.Label(root, text = "My Label",bootstyle = "warning",font=("Helvetica",19))
my_label.pack()

scroll_text = ScrolledText(root, bootstyle="primary",height=5)
scroll_text.pack(fill=X, pady=20, padx=10)

my_btn = tb.Button(root,text = f"Submit" ,bootstyle = "warning outline")
my_btn.pack(pady=10)

root.mainloop()