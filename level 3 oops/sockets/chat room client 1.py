from tkinter import *
from threading import Thread
import socket
host='localhost'
port= 12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#s.setblocking(False)  # Set non-blocking mode



root=Tk()
msgframe=Frame(root, height= 150)
loginframe=Frame(root)
loginframe.pack(side=TOP)
user=Label(loginframe, text="ENTER your username")
user.pack()
enteringuser=Entry(loginframe)
enteringuser.pack(fill=X)

def login():
    username=enteringuser.get()
    s.connect((host,port))
    print("connected")
    loginframe.pack_forget()
    root.title(username)
    s.sendall(username.encode())
    msgframe.pack(side=TOP, fill=X)
    enter.pack(fill=X)
    send.pack(fill=X)
    recp_thread=Thread(target=receive_messages)
    recp_thread.start()


def receive_messages():
    while True:
        try: 
            message=s.recv(1024).decode()
            chat=Label(msgframe, text=message, anchor="w")
            chat.pack(side=TOP, fill=X)
        except ConnectionResetError:
            print("server disconnected, trying to reconnect")
            try:
                s.connect((host,port))
                print("reconnected")
            except:
                print("could not reconnect")
                break
        except:
            break



loginbutton=Button(loginframe, text="LOGIN", command=login)
loginbutton.pack(fill=X)


def send_data():
    data=enter.get()
    s.sendall(data.encode())
    enter.delete(0, END)

     

def on_closing():
    s.close()
    root.destroy()
    


enter=Entry(root)

send=Button(root, text="Send", command=send_data)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()