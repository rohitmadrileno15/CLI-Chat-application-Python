import socket
import pyfiglet
import pycrypt
from time import sleep
import random
result = pyfiglet.figlet_format("Encrypted Chat", font = "slant"  )
print(result)

HEADER = 256
# needs to be updated
flag = True
while(flag):
    usr_name = str(input("Enter any name \n"))
    usr_name = usr_name.strip()
    if(len(usr_name)==0):
        print("Enter a valid user name!")
    else:
        flag = False


PORT = 5050
FORMAT='utf-8'
DICONNECT_MSG = "DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_len = str(msg_length).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

print("if you want to exit, type in 'exit' ")

print("<----------->")
connection_condition = True

while(connection_condition):


    msg_to_server = str(input("enter msg \n"))
    msg_to_server = msg_to_server.strip()
    if(len(msg_to_server)==0):
        print("Enter any value")
        continue


    order = ['exit', 'Exit', 'EXIT']

    if(msg_to_server in order):
        send(DICONNECT_MSG)
        print("You will now exit from the chat!")
        time.sleep(2)
        break

    rand_val =  15

    msg_to_server = usr_name + " :- " + msg_to_server
    for i in range(rand_val):
        msg_to_server = pycrypt.caesar.encrypt(msg_to_server, 5)

    send(msg_to_server)
    print("-------message sent---------")
    print()
    client.send("PING".encode(FORMAT))

    data = client.recv(1024).decode(FORMAT)
    for i in range(rand_val):
        data = pycrypt.caesar.decrypt(data, 5)
    print(data)
    print("-------------------")
