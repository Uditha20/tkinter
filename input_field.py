from tkinter import *


root=Tk()

#create  the input field
e=Entry(root,width=50)
e.pack()
e.insert(0,"enter your name")

def clickme():
    my_label=Label(root,text=e.get()) #get function get the user input
    my_label.pack()

my_b=Button(root,text='click me',command=clickme)
my_b.pack()

root.mainloop()