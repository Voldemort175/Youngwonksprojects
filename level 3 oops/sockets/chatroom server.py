from tkinter import *
from threading import Thread
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=''
port= 12345
s.bind((host,port))
s.listen(5)
print("Socket is listening")
allusers={}




def accept_conn():
    global allusers
    while True:
        conn,addr=s.accept()
        print("got a connection from", addr)
        username=conn.recv(1024).decode()
        allusers[username]=conn
        if len(allusers)>0:
            print(allusers) 
        send_everyone((username+" has joined the chat"))
        temp_thread=Thread(target=listener, args=(conn,username))
        temp_thread.start()

def send_everyone(message):
    for user , conn in allusers.items():
        try:
            conn.sendall(message.encode())
        except:
            print("Error sending message to", user)
            del allusers[user]
def listener(conn, username):
    while True:
        try:
            message=conn.recv(1024).decode()
            send_everyone(("<" + username+ ">: " + message))
        except:
            send_everyone((username + "has left the chat"))
            del allusers[username]
            return 

        
accept_conn()