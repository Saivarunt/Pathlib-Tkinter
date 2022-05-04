import tkinter as tk
from tkinter import *
import main as m
from ufiles import *
from main import *
import pandas as pd
import matplotlib.pyplot as plt

root=Tk()
root.title('File manager with pathlib')

x=list(pd.Series(m.df['Parent']).unique())
itemlst=list()

def tkcall():
    def plot():
        data=pd.read_csv('out.csv')
        plt.scatter(data['Type'],data['File'])
        plt.show()

    def save():
        df=pd.DataFrame(itemlst,columns=['File','Type'])
        df.to_csv('out.csv')

    def visualize():
        df=pd.DataFrame(itemlst,columns=['File','Type'])
        df.to_csv('out.csv')
        plot()

    def computate(f,s):
        global itemlst
        def clear():
            list = root.grid_slaves()
            for l in list:
                l.destroy()
            tkcall()
        def choiceselection(event):
            cval=StringVar()
            cval=cvar.get()
            if str(cval)=='Yes':
                ivar=StringVar()
                ivar.set('')

                label5=Label(root,text="Added files")
                label5.grid(row=6,column=0)

                item=OptionMenu(root,ivar,*itemlst)
                item.grid(row=6,column=1)
                
                b1=Button(root,text='Select more files',command=clear)
                b1.grid(row=5,column=1)
            elif str(cval)=='No':
                saveb=Button(root,text='Save files',command=save)
                saveb.grid(row=5,column=0)

                savebv=Button(root,text='Save & Visualize',command=visualize)
                savebv.grid(row=5,column=1)

                b2=Button(root,text='Exit',command=lambda: root.destroy())
                b2.grid(row=5,column=2)
        
        itemlst.append((f,s))
        chc=['Yes','No']

        cvar=StringVar()
        cvar.set('')

        label4=Label(root,text="Do you want to add more files?")
        label4.grid(row=4,column=0)

        choice=OptionMenu(root,cvar,*chc,command=choiceselection)
        choice.grid(row=4,column=1)

        

    def val(s):
        def ft():
            def fils(event):
                fileval=StringVar()
                fileval=filevar.get()
                computate(fileval,s)
            filevar=StringVar()
            filevar.set('')
    
            label3=Label(root,text="--Available Files In Directory--")
            label3.grid(row=3,column=0)

            filelabel=OptionMenu(root,filevar,*fls,command=fils)
            filelabel.grid(row=3,column=1)
        fls=[]
        p=pathlib.Path(dvar.get())
        for i in p.glob('*'+s):
            fls.append(i)
        ft()


    def ufs(s):
        def suffix(event):
            uval=StringVar()
            uval=uvar.get()
            val(uval)
        uvar=StringVar()
        uvar.set("Select a file type")

        label2=Label(root,text="--File Type--")
        label2.grid(row=2,column=0)

        dropbutton2=OptionMenu(root,uvar,*s,command=suffix)
        dropbutton2.grid(row=2,column=1)


    def directory(event):
        dirval=StringVar()
        dirval=dvar.get()

        suflst=list()   
        indx=0
        for i in m.df['Parent'].values:
            if i==pathlib.Path(dirval):
                j=m.df['Suffix'].values[indx]
                suflst.append(j)
            indx=indx+1
        usuflst=list(pd.Series(suflst,dtype=str).unique())

        ufs(usuflst)


    dvar=StringVar()
    dvar.set("Select directory")

    label1=Label(root,text="--Directory--")
    label1.grid(row=0,column=0)

    dropbutton1=OptionMenu(root,dvar,*x,command=directory)
    dropbutton1.grid(row=0,column=1)

def plot():
    data=pd.read_csv('out.csv')
    plt.scatter(data['Type'],data['File'])
    plt.show()


def save():
    df=pd.DataFrame(itemlst,columns=['File','Type'])
    df.to_csv('out.csv')

def visualize():
    df=pd.DataFrame(itemlst,columns=['File','Type'])
    df.to_csv('out.csv')
    plot()



def computate(f,s):
    global itemlst
    def clear():
        list = root.grid_slaves()
        for l in list:
            l.destroy()
        tkcall()
    def choiceselection(event):
        cval=StringVar()
        cval=cvar.get()
        if str(cval)=='Yes':
            ivar=StringVar()
            ivar.set('')

            label5=Label(root,text="Added files")
            label5.grid(row=6,column=0)

            item=OptionMenu(root,ivar,*itemlst)
            item.grid(row=6,column=1)

            b1=Button(root,text='Select more files',command=clear)
            b1.grid(row=5,column=1)

        elif str(cval)=='No':
            saveb=Button(root,text='Save files',command=save)
            saveb.grid(row=5,column=0)

            savebv=Button(root,text='Save & Visualize',command=visualize)
            savebv.grid(row=5,column=1)         
            
            b2=Button(root,text='Exit',command=lambda: root.destroy())
            b2.grid(row=5,column=2)
    itemlst.append((f,s))
    chc=['Yes','No']

    cvar=StringVar()
    cvar.set('')

    label4=Label(root,text="Do you want to add more files?")
    label4.grid(row=4,column=0)

    choice=OptionMenu(root,cvar,*chc,command=choiceselection)
    choice.grid(row=4,column=1)


        

def val(s):
    def ft():
        def fils(event):
            fileval=StringVar()
            fileval=filevar.get()
            computate(fileval,s)
        filevar=StringVar()
        filevar.set('')
    
        label3=Label(root,text="--Available Files In Directory--")
        label3.grid(row=3,column=0)

        filelabel=OptionMenu(root,filevar,*fls,command=fils)
        filelabel.grid(row=3,column=1)
    fls=[]
    p=pathlib.Path(dvar.get())
    for i in p.glob('*'+s):
        fls.append(i)
    ft()


def ufs(s):
    def suffix(event):
        uval=StringVar()
        uval=uvar.get()
        val(uval)
    uvar=StringVar()
    uvar.set("Select a file type")

    label2=Label(root,text="--File Type--")
    label2.grid(row=2,column=0)

    dropbutton2=OptionMenu(root,uvar,*s,command=suffix)
    dropbutton2.grid(row=2,column=1)


def directory(event):
    dirval=StringVar()
    dirval=dvar.get()

    suflst=list()   
    indx=0
    for i in m.df['Parent'].values:
        if i==pathlib.Path(dirval):
            j=m.df['Suffix'].values[indx]
            suflst.append(j)
        indx=indx+1
    usuflst=list(pd.Series(suflst,dtype=str).unique())

    ufs(usuflst)


dvar=StringVar()
dvar.set("Select directory")

label1=Label(root,text="--Directory--")
label1.grid(row=0,column=0)

dropbutton1=OptionMenu(root,dvar,*x,command=directory)
dropbutton1.grid(row=0,column=1)

tk.mainloop()