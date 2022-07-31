from tkinter import *


root=Tk()
root.title("calculator")
root.geometry("400x400")

def addme():
    number_1=e.get()
    number_2=f.get()
    total=int(number_1)+int(number_2)

    my_label=Label(root,text=total)
    my_label.pack()

e=Entry(root,borderwidth=5)
e.pack()

f=Entry(root)
f.pack()

my_button=Button(root,text="click me",command=addme)
my_button.pack()

root.mainloop()