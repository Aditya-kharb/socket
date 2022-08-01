import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP = '25.18.33.109'
PORT = 1234
s.connect((IP,PORT))
for x in range(0,3):
    msg = s.recv(1000) 
    print(IP+" said =>"+msg.decode('utf-8'))
    ask_input = input("enter message:")
    s.send(bytes(ask_input,'utf-8'))