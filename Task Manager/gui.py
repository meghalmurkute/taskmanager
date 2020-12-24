import tkinter
from tkinter import *
from tkinter import messagebox
import dbhelper
from datetime import datetime
import os

def deletetask(event):
    task=listbox.get(ANCHOR)
    for rows in dbhelper.showtask(task):
        MsgBox = messagebox.askquestion ('Delete '+task ,'Are you sure you want to delete ' + rows[1] + ' ' + rows[2] + ' ' + rows[3],icon = 'warning')
        if MsgBox == 'yes':
            dbhelper.deletebytask(task)
    populate()
    notify()
    
def populate():
    listbox.delete(0, END)
    for rows in dbhelper.show():
        listbox.insert(END, rows[1])
    
def notify():
    now = datetime.now()
    sysdate = now.strftime("%d/%m/%Y")
    systime = now.strftime("%H:%M")
    for rows in dbhelper.show():
        task = rows[1]
        date = rows[2]
        time = rows[3]
        if date == sysdate and time == systime:
            MsgBox= messagebox.showinfo(
                "Alert!!!", "Your task: "+task )
            if MsgBox == 'ok':
                dbhelper.deletebytask(task)
                populate()
                notify()
        if date == sysdate and time < systime:
            MsgBox= messagebox.showerror(
                "Missed!!!", "You missed "+task+" task" )
            if MsgBox == 'ok':
                dbhelper.deletebytask(task)
                populate()
                notify()

def text():
    main.destroy()
    os.system('python text.py')
    
    
def voice():
    main.destroy()
    os.system('python voice.py')
    
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

addbtn = tkinter.Button(
    addframe,
    text="Text",
    command=text,
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

addbtn = tkinter.Button(
    addframe,
    text="Voice",
    command=voice,
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

refreshbtn = tkinter.Button(
    addframe,
    text="REFRESH",
    command=notify,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
refreshbtn.pack(padx=20, pady=10, ipadx=20, ipady=5)

tkinter.Label(
    main,
    text="Your Tasks",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Calibri", 18),
).pack(pady=10)

taskframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
taskframe.pack(fill=BOTH, expand=300)
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(
    taskframe,
    font=("Verdana 18 bold"),
    bg="#1d1d1d",
    fg="#eeeeee",
    selectbackground="#eeeeee",
    selectforeground="#1d1d1d",
)
listbox.pack(fill=BOTH, expand=300)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.bind("<Double-Button-1>", deletetask)
listbox.bind("<Delete>", deletetask)

populate()
notify()


tkinter.Label(
    main,
    text="TIP : Double Click On A Task to Delete",
    background="#1d1d1d",
    foreground="#FFEB3B",
    font=("Calibri 18"),
).pack(side=BOTTOM, pady=10)

main.mainloop()
