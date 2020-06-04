import socket
import threading
import sys
from time import sleep

result = ("*** Encrypted Chat Application ***")

print(result)

print()
print()
HEADER = 256
# needs to be updated

PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())
print("server address" , SERVER)
print()
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# the above line means the socket method, socket type
server.bind(ADDR)
FORMAT='utf-8'
DICONNECT_MSG = "DISCONNECT"


msg_list = []


def handle_client(conn,addr):


    print("NEW USER-->", addr , "connected")
    with open("logs.txt", "a") as f:
         f.write("New User Connected \n")
    connected = True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if (msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if (msg == DICONNECT_MSG):
                connected = False
                print("One User has disconnected")
                with open("logs.txt", "a") as f:
                     f.write("User disconnected \n")

            print(msg)
            msg_list.append(msg)

            print(msg_list)
            r="\n".join(msg_list)
            data__ = conn.recv(1024).decode(FORMAT)

            if(data__ == "PING"):
                conn.send(r.encode(FORMAT))




    conn.close()



def start ():
    server.listen()
    print()
    print("looking for msgs")
    with open("logs.txt", "a") as f:
         f.write("Looking for new msgs \n \n")
    while (True):

        try:

            conn , addr = server.accept()
            thread = threading.Thread(target=handle_client, args =(conn,addr))
            thread.start()

            connection_number = (threading.activeCount() -1)

            print("ACTIVE CONNECTIONS - ", connection_number)
            with open("logs.txt", "a") as f:
                 f.write("ActiveUsers" + str(connection_number) +"\n")
            if(connection_number>21):
                print("User limit exceeded")
                time.sleep(3)
                server.close()
                print("Connection closed")
                with open("logs.txt", "a") as f:
                     f.write("Encountered Error!\n")

                sys.exit()


        except Exception as e:
            with open("logs.txt", "a") as f:
                 f.write("Encountered Error! as" + str(e)+ "\n")





print("STARTING -->")
start()
