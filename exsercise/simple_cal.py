from tkinter import *

root=Tk()
root.title("cal")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def addme(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return

def clear():
    e.delete(0,END)

def add_num():
    number_1=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(number_1)
    e.delete(0,END)

def equal():
    number_2=e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num+int(number_2))

    if math == "substration":
        e.insert(0,f_num-int(number_2))

    if math == "multiply":
        e.insert(0,f_num*int(number_2))

    if math == "division":
        e.insert(0,f_num/int(number_2))

def multiply():
    number_1=e.get()
    global f_num
    global math
    math="multiply"
    f_num=int(number_1)
    e.delete(0,END)

def substraction():
    number_1=e.get()
    global f_num
    global math
    math="substration"
    f_num=int(number_1)
    e.delete(0,END)

def division():
    number_1=e.get()
    global f_num
    global math
    math="division"
    f_num=int(number_1)
    e.delete(0,END)


button_1=Button(root,text="1",padx=40,pady=20,command=lambda: addme(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: addme(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: addme(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: addme(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: addme(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: addme(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: addme(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: addme(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: addme(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: addme(0))

button_10=Button(root,text="+",padx=40,pady=20,command=add_num)
button_11=Button(root,text="C",padx=40,pady=20,command=clear)

button_12=Button(root,text="=",padx=140,pady=20,command=equal)

button_13=Button(root,text="*",padx=40,pady=20,command=multiply)
button_14=Button(root,text="-",padx=40,pady=20,command=substraction)
button_15=Button(root,text="/",padx=40,pady=20,command=division)




button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_10.grid(row=4,column=1)
button_11.grid(row=4,column=2)

button_13.grid(row=5,column=0)
button_14.grid(row=5,column=1)
button_15.grid(row=5,column=2)
button_12.grid(row=6,column=0,columnspan=3)



root.mainloop()
