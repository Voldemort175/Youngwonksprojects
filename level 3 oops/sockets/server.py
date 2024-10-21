import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=''
port= 12345
s.bind((host,port))
s.listen(5)
print("Socket is listening")
conn,addr=s.accept()

print("got a connection from", addr)