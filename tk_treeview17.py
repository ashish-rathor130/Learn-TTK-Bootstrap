from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Ttk Treeview")
root.geometry("400x600")


my_label =tb.Label(root, text = "My Treeview",bootstyle = "info")
my_label.pack(pady=10)

columns = ["name","email","phone"]

my_tree = tb.Treeview(root, columns=columns,bootstyle = "warning", show="headings")
my_tree.pack(pady=10 , padx = 10)

"defining headings"

my_tree.heading("name",text = "Name")
my_tree.heading("email",text = "Email")
my_tree.heading("phone",text = "Phone")

"creating sample data"

mydata = []
for item in range(10):
    mydata.append((f"name {item}",f"email@{item}.com", f"phone{item}"))

"add data to treeview"

for data in mydata:
    my_tree.insert("",END, values= data)





root.mainloop()
