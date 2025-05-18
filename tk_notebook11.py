from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap")
root.geometry("540x350")

my_notebook = tb.Notebook(root,bootstyle = "info")
my_notebook.pack(fill="both")

tab1 = tb.Frame(my_notebook,bootstyle = "light")
tab2 = tb.Frame(my_notebook,bootstyle = "light")

f1 = tb.Label(tab1,text = "Tab 1",bootstyle = "")
f1.pack()

text1 = tb.Text(tab1,height=5,width=30)
text1.pack(padx=5,pady=5)

btn1 = tb.Button(tab1,text = "Click me!" , bootstyle = "info outline")
btn1.pack(padx=5,pady=5)

f1 = tb.Label(tab2,text = "Tab 2",bootstyle = "")
f1.pack()

my_notebook.add(tab1,text="Tab 1")
my_notebook.add(tab2,text="Tab 2")
root.mainloop()