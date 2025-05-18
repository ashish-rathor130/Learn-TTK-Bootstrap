from tkinter import * 
import ttkbootstrap as tb

root = tb.Window(themename="vapor")
root.title("add the img")
root.geometry("400x600")

photo = tb.PhotoImage(file = "./education.png")

my_frame = tb.Frame(root,bootstyle = "light")
my_frame.pack(padx=20, pady=20)

my_img_label = tb.Label(my_frame, image=photo,bootstyle = "")
my_img_label.pack(padx = 20, pady=20)

my_label = tb.Label(my_frame, text = "Education Image")
my_label.pack(pady=10)


root.mainloop()