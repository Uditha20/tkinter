from tkinter import *
from tkinter import ttk


root=Tk()

# my_label=Label(root,text="hello world").grid(row=0,column=0)
# my_label_1=Label(root,text="uditha indunil").grid(row=1,column=0)

def myclick():
    my_label=Label(root,text="hello world")
    my_label.pack()

mybutton=Button(root,text="clickme",command=myclick,fg="blue",bg="red") #create the button
mybutton.pack()

# my_label.grid(row=0,column=0)
# my_label_1.grid(row=1,column=0)


#my_label.pack()

root.mainloop()