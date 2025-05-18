from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename = "vapor")
root.title("TTk Menubutton")
root.geometry("500x600")

def sel(x):
    menu.config(bootstyle=f"{x}")
menu = tb.Menubutton(root,text="menu",bootstyle="info")
menu.pack()

list = tb.Menu(menu)

v = StringVar()

for x in "info warning secondary primary".split():
    list.add_radiobutton(label=x,variable=v, command=lambda x= x:sel(x))

menu['menu']=list

root.mainloop()