from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x350")

def clicker(e):
    my_scale.config(text = f"Your scale is {int(my_slider.get())}")

my_label = tb.Label(root,text = "Select the Scale", bootstyle ="info", font = ("Helvetica",20))
my_label.pack(pady=20)

my_slider = tb.Scale(root,bootstyle = "info",from_= 0 ,length=400, to=100,value = 0,orient= "horizontal",command = clicker)
my_slider.pack(pady=20)

my_scale = tb.Label(root, text = "",bootstyle = "warning" , font = ("Helvetica",15))
my_scale.pack(pady=10,padx = 10)


root.mainloop()