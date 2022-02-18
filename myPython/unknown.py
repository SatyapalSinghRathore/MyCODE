from tkinter import*

root=Tk()
root.geometry('100x100')
def a(event):
    print('hello')
c=Canvas(width=20,height=20,bg='black')
c.pack()
c.create_rectangle(5,4,9,8,fill='white')
c.create_rectangle(5,9,9,13,fill='white')
c.create_rectangle(5,14,9,18,fill='white')

c.create_rectangle(10,4,19,8,fill='white')
c.create_rectangle(10,9,19,13,fill='white')
c.create_rectangle(10,14,19,18,fill='white')

c.bind('<Key>',a)


root.mainloop()