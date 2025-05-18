import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.toast import ToastNotification

root = tb.Window(themename="superhero")
root.title("TTk MessBox")
root.geometry("600x600")

def gettoast():
    my_toast.show_toast()

my_label = tb.Label(root,text = "Toast Message!",font  = ("Helvetica",16))
my_label.pack(pady=20)

my_toast = ToastNotification(
    title="Toast Notification",
    message="This is a toast message!",
    duration=3000,
    alert=True,
    position=(145,60,"sw"),
)

my_btn = tb.Button(root,text="Get Toast",bootstyle="info outline",command=gettoast)
my_btn.pack(pady=20)


root.mainloop()