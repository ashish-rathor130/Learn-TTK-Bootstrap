import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.dialogs  import Messagebox

root = tb.Window(themename="superhero")
root.title("TTk MessBox")
root.geometry("600x500")

def ok():
    Messagebox.ok("Ok Message!","This is an Ok message")
def yesno():
    Messagebox.yesno("Yes No Message","This is a Yes No message")
def okcancel():
    Messagebox.okcancel("Ok Cancel Message","This is an Ok Cancel message")
def yesnocancel():
    Messagebox.yesnocancel("Yes No Cancel Message","This is a Yes No Cancel message")
def retrycancel():
    Messagebox.retrycancel("Retry Cancel Message","This is a Retry Cancel message")
def showinfo():
    Messagebox.show_info("Show Info Message","This is a Show Info message")
def showwarning():
    Messagebox.show_warning("Show Warning Message","This is a Show Warning message")
def showerror():
    Messagebox.show_error("Show Error Message","This is a Show Error message")
def showquestion():
    Messagebox.show_question("Show Question Message","This is a Show Question message")




my_label = tb.Label(root, text = "My MessBox",bootstyle = "warning", font = ("Helvetica",12))
my_label.pack(pady=10)
my_label = tb.Label(root, text = "(yesno, ok, okcancel, yesnocancel,retrycancel)",bootstyle = "warning", font = ("Helvetica",10))
my_label.pack(pady=10)
my_label = tb.Label(root, text = "show_warning, show_info, show_error,show_question)",bootstyle = "warning", font = ("Helvetica",10))
my_label.pack(pady=10)

btn_frame = tb.Frame(root)
btn_frame.pack(pady=5, padx=5)

my_btn = tb.Button(btn_frame, text ="Ok", command=ok, bootstyle = "info outline")
my_btn.grid(row = 0, column = 0, padx=5)
my_btn = tb.Button(btn_frame, text ="YesNo", command=yesno, bootstyle = "warning outline")
my_btn.grid(row = 0, column = 1, padx=5)
my_btn = tb.Button(btn_frame, text ="OkCancel", command=okcancel, bootstyle = "success outline")
my_btn.grid(row = 0, column = 2, padx=5)
my_btn = tb.Button(btn_frame, text ="YesNoCancel", command=yesnocancel, bootstyle = "primary outline")
my_btn.grid(row = 0, column = 3, padx=5)
my_btn = tb.Button(btn_frame, text ="RetryCancel", command=retrycancel, bootstyle = "secondary outline")
my_btn.grid(row = 2, column = 1, padx=5)

my_btn = tb.Button(btn_frame, text ="ShowInfo", command=showinfo, bootstyle = "light outline")
my_btn.grid(row = 1, column = 0, padx=5 ,pady = 5)
my_btn = tb.Button(btn_frame, text ="ShowWarning", command=showwarning, bootstyle = "primary outline")
my_btn.grid(row = 1, column = 1, padx=5, pady = 5)
my_btn = tb.Button(btn_frame, text ="ShowError", command=showerror, bootstyle = "danger outline")
my_btn.grid(row = 1, column = 2, padx=5, pady = 5)
my_btn = tb.Button(btn_frame, text ="ShowQuestion", command=showquestion, bootstyle = "warning outline")
my_btn.grid(row = 1, column = 3, padx=5, pady = 5)




root.mainloop()