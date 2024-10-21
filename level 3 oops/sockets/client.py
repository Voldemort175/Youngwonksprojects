import socket
host='localhost'
port= 12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

print("connected")