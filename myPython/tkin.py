from tkinter import * 
from datetime import date
from PIL import Image

root=Tk()
root.geometry('733x434')
root.minsize(400,300)
root.title('Newspaper')
date1=Label(text=f'DATE: {date.today()}',bg='gray',pady=4,font='comicsansam 15 bold')
date1.pack(side=TOP,anchor='nw')
title1=Label(text='TIMES OF INDIA',bg='black',fg='lightblue',pady=70,font='palatino 40 bold')
title1.pack(fill=X)
f1 = Frame(root, bg='black', borderwidth=4,padx=23,pady=10)
f1.pack(side=BOTTOM, fill=X)
b1 = Button(f1, text='<',fg='white',bg='black',command=None)
b1.pack(side=LEFT,fill=Y)
b1.place(x=500,y=2)
botom=Label(f1,text='-- HERE YOU GET LATEST NEWS --',bg='black',fg='white',pady=3,font='comicsansam 10 bold')
botom.pack(side=TOP)
b2 = Button(f1, text='>',fg='white',bg='black',command=None)
b2.pack(side=RIGHT,fill=Y)
b2.place(x=793,y=2)
img=PhotoImage(file='e.png')
im=Label(image=img,borderwidth=10,relief=RIDGE)
im.pack(side=LEFT, anchor='w')
artical=Label(text='One of our era\'s greatest scourges is air pollution,\n on account not only of its impact on climate change but\n also its impact on public and individual health due to increasing morbidity\n and mortality. There are many pollutants that\n are major factors in disease in humans. Among them, \nParticulate Matter (PM), particles of variable but very small diameter,\n penetrate the respiratory system via inhalation, causing respiratory\n and cardiovascular diseases, reproductive\n and central nervous system dysfunctions, and cancer.',bg='gray',fg='black',font='comicsansam 13 bold',padx=30,pady=34)
artical.pack(side=RIGHT)
artical.place(x=650,y=270)


root.mainloop()