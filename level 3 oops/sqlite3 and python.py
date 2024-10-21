import sqlite3
conn=sqlite3.connect("login.db")
c=conn.cursor()
#c.execute("CREATE TABLE Users (UserID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT NOT NULL,Username TEXT NOT NULL UNIQUE,Password TEXT NOT NULL)")
#c.execute(" INSERT INTO Users (Name, Username, Password) VALUES ('John Doe', 'johndoe', 'password123'), ('Jane Smith', 'janesmith', 'password123'), ('Bob Johnson', 'bobjohnson', 'password123')")
#conn.commit()
# c.execute('SELECT * FROM Users')
# for row in c:
#     print(row)
#     print(type(c))


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
notebook=ttk.Notebook(root)


def add():
    
    username = userentry2.get()
    password = passentry2.get()
    c.execute("SELECT Username from USERS WHERE Username=?",(username,))
    if c.fetchone() is None:    # if a row is not found, username doesn't exist already
        c.execute("INSERT INTO Users (Name, Username, Password) VALUES (?,?,?)",(username,username,password))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully")
    else:
        messagebox.showerror("Error", "Username already exists")

def login():
    
    username = userentry.get()
    password = passentry.get()
    c.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (username,password))
    if c.fetchone():
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")

frame1=Frame(notebook)
frame2=Frame(notebook)
userlabel=Label(frame1,text="Username")
userentry=Entry(frame1)
passlabel=Label(frame1,text="Password")
passentry=Entry(frame1,show="*")

submit=Button(frame1,text="Submit", command=login)


userlabel.pack()
userentry.pack()
passlabel.pack()
passentry.pack()
submit.pack()

userlabel2=Label(frame2,text="Username")
userentry2=Entry(frame2)
passlabel2=Label(frame2,text="Password")
passentry2=Entry(frame2,show="*")

Register=Button(frame2,text="Register",command=add)


userlabel2.pack()
userentry2.pack()
passlabel2.pack()
passentry2.pack()
Register.pack()


notebook.add(frame1,text="login")
notebook.add(frame2,text="register")
notebook.pack()



root.mainloop()