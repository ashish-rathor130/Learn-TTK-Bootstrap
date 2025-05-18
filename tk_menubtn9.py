from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename = "vapor")
root.title("TTk Menubutton")
root.geometry("500x600")

def menu_selection(item):
    menu_btn.config(bootstyle = f"{item}")
menu_btn = tb.Menubutton(root, text="Menu Button",bootstyle = "warning")
menu_btn.pack(pady=10)

menu_list = tb.Menu(menu_btn)

var1 = StringVar()
for item in ["primary","secondary","info","warning","success","danger"]:
    menu_list.add_radiobutton(label=item, command=lambda item=item:menu_selection(item),variable= var1)

menu_btn['menu'] = menu_list

root.mainloop()