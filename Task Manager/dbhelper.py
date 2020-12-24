import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL
);''')

def show():
    query = "SELECT * FROM todo;"
    return conn.execute(query)

def showtask(task):
    query = "SELECT * FROM todo where task=?;"
    return conn.execute(query, (task,))

def insertdata(task, date, time):
    query = "INSERT INTO todo(task, date, time) VALUES(?, ?, ?);"
    conn.execute(query, (task, date, time,))
    conn.commit()


def deletebyid(taskid):
    query = "DELETE FROM todo WHERE id =?;"
    conn.execute(query, (taskid,))
    conn.commit()

def deletebytask(taskval):
    query = "DELETE FROM todo WHERE task =?;"
    conn.execute(query, (taskval,))
    conn.commit()


def updatedata(taskid, newtask):
    query = "UPDATE todo SET task = ? WHERE id = ?;"
    conn.execute(query, (newtask, taskid))
    conn.commit()
