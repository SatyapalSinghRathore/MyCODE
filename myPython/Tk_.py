from tkinter import * 
from PIL import Image, ImageTk
from time import sleep
import wikipedia

root=Tk()
root.geometry('300x500')
im=Image.open('3.png')
im=im.resize((20,20))
im=ImageTk.PhotoImage(im)
root.iconphoto(False,im)
root.maxsize(300,500)
root.title('Message')
root['bg']='#1a1a1a'

im2=Image.open('search.png')
im2=im2.resize((20,20))
im2=ImageTk.PhotoImage(im2)
im3=Image.open('home.png')
im3=im3.resize((20,20))
im3=ImageTk.PhotoImage(im3)

value=0
def a():
    global value
    if value==0:
        for i in range(-50,1):
            f2.place(x=i,y=30)
            f1.update()
        value=1
    else:
        for i in range(0,51):
            f2.place(x=-i,y=30)
            f1.update()
        value=0

value1=StringVar()
def b():
    global value
    if value==1:
        for i in range(0,51):
            f2.place(x=-i,y=30)
            f1.update()
        value=0
        Entry(f1,bg='#0d0d0d',textvariable=value1,fg='yellow').pack(side=LEFT)
        Button(f1,text='Search',bg='black',activebackground='yellow',activeforeground='black',command=lambda :d(value1.get()),fg='yellow',bd=0,padx=5).pack(side=LEFT)

def d(value1):
    result=wikipedia.summary(value1,sentences=2)
    result=result.replace(' ','\n')
    # print(result)
    Label(root,text=result,bg='#1a1a1a',fg='yellow').pack()

root.minsize(300,500)
f1=Frame(bg='#1a1a1a')
f1.pack(side=TOP,fill=X)
b1=Button(f1,text='. . .',fg='white',font='impact',activebackground='yellow',bd=0,bg='black',padx=14,command=a)
b1.pack(side=LEFT)
f2=Frame(root,bg='black',width=50,height=500)
f2.place(x=-50,y=30)
Button(f2,image=im2,bg='black',activebackground='black',bd=0,padx=5,command=b).place(x=12,y=10)
Button(f2,image=im3,bg='black',activebackground='black',bd=0,padx=5).place(x=12,y=50)

root.mainloop()