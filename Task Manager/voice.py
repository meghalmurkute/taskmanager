import tkinter
from tkinter import *
from tkinter import messagebox
import dbhelper
from datetime import datetime
import os
import speech_recognition as sr


def doSomething():
    main.destroy()
    os.system('python gui.py')

def add():
    if(len(addtask.get()) == 0):
        messagebox.showerror(
            "ERROR", "No data Available\nPlease Enter Some Task")
    else:
        dbhelper.insertdata(addtask.get(), adddate.get(), addtime.get())
        addtask.delete(0, END)
        adddate.delete(0, END)
        addtime.delete(0, END)
        doSomething()      
    
def notify():
    now = datetime.now()
    sysdate = now.strftime("%d/%m/%Y")
    systime = now.strftime("%H:%M")
    for rows in dbhelper.show():
        task = rows[1]
        date = rows[2]
        time = rows[3]
        if date == sysdate and time == systime:
            messagebox.showinfo(
                "Alert", "Your task:"+task )

def addtsk():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
 
        # recognize speech using google
        addtask.insert(0, r.recognize_google(audio))
    
def adddt():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
        # recognize speech using google
        x=str(r.recognize_google(audio))
        y=x.split()
        mth={"january":"01", "february":"02", "march":"03", "april":"04", "may":"05", "june":"06", "july":"07", "august":"08", "september":"09", "october":"10", "november":"11", "december":"12"}
        sm=y[1].lower()
        mt=mth[sm]
        a=y[0]+"/"+mt+"/"+y[2]
        adddate.insert(0, a)

    
main = tkinter.Tk()
main.title("TODO")
main.geometry("500x600")
main.resizable(False, False)
main.configure(
    background="#1d1d1d",
)

tkinter.Label(
    main,
    text="Task Manager",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

addframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
addframe.pack()

tkinter.Label(
    addframe,
    text="Task",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

addtask = tkinter.Entry(
    addframe,
    font=("Verdana"),
    background="#eeeeee",
)
addtask.pack(padx=30, ipadx=20, ipady=5)

addbtntsk = tkinter.Button(
    addframe,
    text="ADD TASK",
    command=addtsk,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
addbtntsk.pack(padx=20, pady=10, ipadx=20, ipady=5)

tkinter.Label(
    addframe,
    text="Date say 12 August 2020",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

adddate = tkinter.Entry(
    addframe,
    font=("Verdana"),
    background="#eeeeee",
)
adddate.pack(padx=30, pady=10, ipadx=20, ipady=5)

addbtndate = tkinter.Button(
    addframe,
    text="ADD DATE",
    command=adddt,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
addbtndate.pack(padx=20, pady=10, ipadx=20, ipady=5)

tkinter.Label(
    addframe,
    text="Time HH:MM",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

addtime = tkinter.Entry(
    addframe,
    font=("Verdana"),
    background="#eeeeee",
)
addtime.pack(padx=30, ipadx=20, ipady=5)

addbtn = tkinter.Button(
    addframe,
    text="ADD",
    command=add,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
addbtn.pack(padx=20, pady=10, ipadx=20, ipady=5)
notify()
main.protocol('WM_DELETE_WINDOW', doSomething) 
main.mainloop()
