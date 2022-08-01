import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = '25.18.33.109'
PORT = 1234
s.bind((IP,PORT))
print("[+] Server connected")
s.listen(10)
client,address = s.accept()
temp_file = []
for x in range(0,3):
    ask_in = input("Now you speak :")
    client.send(bytes(ask_in,"utf-8"))
    msg = client.recv(1000)
    print(address[0]+" said =>"+msg.decode('utf-8'),'\n')
    temp_file.append((f"{msg.decode('utf-8')}",f"{ask_in}"))
print(temp_file)