# CLI Chat application-Python

 Its a CLI application, can be viewed in any machine.
 Before running, check your machine ports and adjust the same with the scripts

 1. First Run the server.py
 2. Then run the client.py as per the number of user's wishes
 3. Note:- server to client CONNECTIONS will close once the active users go above 20 (this can be changed or can be unchecked all over)
 4. Also check the log.txt incase of any errors encountered, log file is properly documented
 5. The Chat is encrypted with a basic caesar cipher, which can be implemented dynamically if the rotations of the cipher encryption and decryption are randomised and handshake exchanged in each message transfer, which will randomise the whole process and the attacker wont be able to guess much considering the cipher texts.
 6. No advanced encryption like RSA or advanced stream ciphers have been used here (check point 5)
 7. However, for an end to end encryptio, one can simply do is, encrypt the msg from the client side and then, send it to server from where it will be broadcasted and when the client recieves the msg, it will decrypt the message using the same key. One can look and say about this from the rsa module of python
 8. Do let me know in case of any error.



 Fewer imports have been done like:-
 import socket,
 import pyfiglet,
 import pycrypt,
 from time import sleep,
 import random,
 import threading,
 import sys
