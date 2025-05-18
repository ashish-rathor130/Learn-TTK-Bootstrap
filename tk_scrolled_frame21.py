import ttkbootstrap as tb 
from tkinter import * 
from ttkbootstrap.scrolled import ScrolledFrame


root = tb.Window(themename="vapor")
root.title("TTk Scrolled Frame")
root.geometry("500x600")

my_label = tb.Label(root, text = "My Label",bootstyle = "warning",font=("Helvetica",19))
my_label.pack()

scroll_frame = ScrolledFrame(root, bootstyle="primary",height=200)
scroll_frame.pack(fill=X, pady=20, padx=10)

for btn in range(20):   
    my_btn = tb.Button(scroll_frame,text = f"Button {btn}" ,bootstyle = "warning outline")
    my_btn.pack(pady=10)

root.mainloop()