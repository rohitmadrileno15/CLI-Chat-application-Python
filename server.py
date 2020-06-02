import socket
import threading

from time import sleep

result = ("Encrypted Chat Application"  )

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
    connected = True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if (msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if (msg == DICONNECT_MSG):
                connected = False
                print("One User has disconnected")
            print(msg)
            msg_list.append(msg)

            print(msg_list)
            r="\n".join(msg_list)
            data__ = conn.recv(1024).decode(FORMAT)
            if(data__ == "PING"):
                conn.send(r.encode(FORMAT))


            # conn.send("Msg sent".encode(FORMAT))

    conn.close()



def start ():
    server.listen()
    print()
    print("looking for msgs")
    while (True):
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client, args =(conn,addr))
        thread.start()
        try:

            connection_number = (threading.activeCount() -1)
            print("ACTIVE CONNECTIONS", connection_number)
            if(connection_number>21):
                print("User limit exceeded")
                time.sleep(3)
                sys.exit()

        except Exception as e:
            print("Its Fine, just a glitch")

        finally:
            print("Encountered Error!")




print("STARTING -->")
start()
