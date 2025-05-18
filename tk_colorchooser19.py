import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.dialogs.colorchooser  import ColorChooserDialog

root = tb.Window(themename="superhero")
root.title("TTk MessBox")
root.geometry("600x600")


def getvalue():
    my_col= ColorChooserDialog()
    my_col.show()

    colors = my_col.result
    my_label.config(text=f"You choose bg color {str(colors.hex)}")

    #set background
    root.configure(background=colors.hex)

my_label = tb.Label(root,text="My Color Chooser(hsv,rgb,hsv)",bootstyle="info",font=("Helvetica",16))
my_label.pack(pady=10)


my_btn = tb.Button(root,text = "Select Color!", command=getvalue,bootstyle="secondary outline round")
my_btn.pack(padx=10,pady=10)

my_label = tb.Label(root,text="",bootstyle="info")
my_label.pack(pady=10)

root.mainloop()