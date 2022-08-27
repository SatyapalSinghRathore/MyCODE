from tkinter import*

root=Tk()
root.geometry('298x464')
root.maxsize(298,464)
root.minsize(298,464)
root.title('Calculator')
root['bg']='black'#a6a6a6


lv0=StringVar()
lv1=StringVar()
lv2=StringVar()
val1=''
val2=''
def press(value):
    global val1
    if val1=='Error':
        val1=''
    val1+=value
    lv2.set(val1)

def remove():
    global val1,val2
    val1=''
    val2=''
    val3=val2
    lv0.set(val3)
    lv1.set(val1)
    lv2.set(val2)

def result():
    global val1,val2
    val3=val2
    val2=val1
    try:
        if 'x' in val1:
            val1=val1.replace('x','*')
            val1=eval(val1)
            if isinstance(val1, float):
                val1=round(val1,2)
                val1=str(val1)
            else:
                val1=str(val1)
        else:
            val1=eval(val1)
            if isinstance(val1, float):
                val1=round(val1,2)
                val1=str(val1)
            else:
                val1=str(val1)
    except:
        val1='Error'
    lv0.set(val3)
    lv1.set(val2)
    lv2.set(val1)
theme1=1
def theme(event):
    global theme1
    list0=[b1,b2,b3,b5,b6,b7,b9,b10,b11,b13,b14,b15,b17,b18]
    list1=[b4,b8,b12,b16]
    list2=[l,l0,l1,l2]
    if theme1==1:
        c['bg']='white'
        f0['bg']='white'
        for i in list2:
            i['bg']='white'
            i['fg']='black'
        for i in list0:
            i['bg']='#c5ccd3'
            i['fg']='black'
        for i in list1:
            i['bg']='#66cdaa'
            i['fg']='black'
            f1['bg']='#a8b3bd'
            f2['bg']='#a8b3bd'
        theme1=2
    elif theme1==2:
        c['bg']='black'
        f0['bg']='black'
        for i in list2:
            i['bg']='black'
            i['fg']='white'
        for i in list0:
            i['bg']='#0d0d0d'
            i['fg']='white'
        for i in list1:
            i['bg']='#c18ff0'
            i['fg']='white'
            f1['bg']='black'
            f2['bg']='black'
            b19['bg']='#6918b4'
        theme1=3
    else:
        for i in list0:
            i['bg']='#0d0d0d'
            i['fg']='white'
        for i in list1:
            i['bg']='#0c271e'
            i['fg']='white'
            f1['bg']='black'
            f2['bg']='black'
            b19['bg']='#0f5753'
        theme1=1

f0=Frame(root,bg='black')
f0.pack(fill=X)
c=Canvas(f0,width=20,height=20,bg='black',highlightthickness=0,relief='ridge')
c.pack(side=LEFT)
c.create_rectangle(5,4,9,8,fill='white')
c.create_rectangle(5,9,9,13,fill='white')
c.create_rectangle(5,14,9,18,fill='white')

c.create_rectangle(10,4,19,8,fill='white')
c.create_rectangle(10,9,19,13,fill='white')
c.create_rectangle(10,14,19,18,fill='white')

c.bind('<Button-1>',theme)
l=Entry(root,bg='black',width=50,fg='white',bd=0,font='impact 15',justify=RIGHT)
l.pack(anchor='nw')
l0=Entry(root,bg='black',textvariable=lv0,width=50,fg='white',bd=0,font='impact 15',justify=RIGHT)
l0.pack(anchor='nw')
l1=Entry(root,bg='black',textvariable=lv1,width=50,fg='white',bd=0,font='impact 25',justify=RIGHT)
l1.pack(anchor='nw')
l2=Entry(root,bg='black',textvariable=lv2,width=50,fg='white',bd=0,font='impact 40',justify=RIGHT)
l2.pack(anchor='nw')
f1=Frame(root,bg='black',width=100,height=490)
f1.pack(anchor='nw')
f2=Frame(root,bg='black',width=100,height=490)
f2.pack(anchor='nw')
b1=Button(f1,text='C',bg='#0d0d0d',fg='white',padx=15,pady=2,font='flat 20',bd=0,command=remove)
b1.grid(row='0',column='0',padx=1,pady=1)
b2=Button(f1,text='+/-',bg='#0d0d0d',fg='white',padx=15,pady=2,font='flat 20',bd=0)
b2.grid(row='0',column='1',padx=1,pady=1)
b3=Button(f1,text='%',bg='#0d0d0d',fg='white',padx=15,pady=2,font='flat 20',bd=0)
b3.grid(row='0',column='2',padx=1,pady=1)
b4=Button(f1,text='+',bg='#0c271e',fg='white',padx=18.5,pady=2,font='flat 20',bd=0,command=lambda: press('+'))
b4.grid(row='0',column='3',padx=1,pady=1)
b5=Button(f1,text='1',bg='#0d0d0d',fg='white',padx=17.5,pady=2,font='flat 20',bd=0,command=lambda: press('1'))
b5.grid(row='1',column='0',padx=1,pady=1)
b6=Button(f1,text='2',bg='#0d0d0d',fg='white',padx=24,pady=2,font='flat 20',bd=0,command=lambda: press('2'))
b6.grid(row='1',column='1',padx=1,pady=1)
b7=Button(f1,text='3',bg='#0d0d0d',fg='white',padx=19,pady=2,font='flat 20',bd=0,command=lambda: press('3'))
b7.grid(row='1',column='2',padx=1,pady=1)
b8=Button(f1,text='-',bg='#0c271e',fg='white',padx=22,pady=2,font='flat 20',bd=0,command=lambda: press('-'))
b8.grid(row='1',column='3',padx=1,pady=1)
b9=Button(f1,text='4',bg='#0d0d0d',fg='white',padx=18,pady=2,font='flat 20',bd=0,command=lambda: press('4'))
b9.grid(row='2',column='0',padx=1,pady=1)
b10=Button(f1,text='5',bg='#0d0d0d',fg='white',padx=23.5,pady=2,font='flat 20',bd=0,command=lambda: press('5'))
b10.grid(row='2',column='1',padx=1,pady=1)
b11=Button(f1,text='6',bg='#0d0d0d',fg='white',padx=19,pady=2,font='flat 20',bd=0,command=lambda: press('6'))
b11.grid(row='2',column='2',padx=1,pady=1)
b12=Button(f1,text='x',bg='#0c271e',fg='white',padx=21,pady=2,font='flat 20',bd=0,command=lambda: press('x'))
b12.grid(row='2',column='3',padx=1,pady=1)
b13=Button(f1,text='7',bg='#0d0d0d',fg='white',padx=18,pady=2,font='flat 20',bd=0,command=lambda: press('7'))
b13.grid(row='3',column='0',padx=1,pady=1)
b14=Button(f1,text='8',bg='#0d0d0d',fg='white',padx=23.5,pady=2,font='flat 20',bd=0,command=lambda: press('8'))
b14.grid(row='3',column='1',padx=1,pady=1)
b15=Button(f1,text='9',bg='#0d0d0d',fg='white',padx=19,pady=2,font='flat 20',bd=0,command=lambda: press('9'))
b15.grid(row='3',column='2',padx=1,pady=1)
b16=Button(f1,text='/',bg='#0c271e',fg='white',padx=23,pady=2,font='flat 20',bd=0,command=lambda: press('/'))
b16.grid(row='3',column='3',padx=1,pady=1)
b17=Button(f2,text='0',bg='#0d0d0d',fg='white',padx=18,pady=2,font='flat 20',bd=0,command=lambda: press('0'))
b17.grid(row='4',column='0',padx=1,pady=1)
b18=Button(f2,text='.',bg='#0d0d0d',fg='white',padx=27.5,pady=2,font='flat 20',bd=0,command=lambda: press('.'))
b18.grid(row='4',column='1',padx=1,pady=1)
b19=Button(f2,text='=',bg='#0f5753',fg='white',padx=55,pady=2,font='flat 20',bd=0,command=result)
b19.grid(row='4',column='2',padx=1,pady=1)

root.mainloop()