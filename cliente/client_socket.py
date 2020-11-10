import socket
from prime_generator import prime_generator
import random
import math
import sys
from BG import public_key_generation, encrypt, decrypt
import time
import datetime
import pickle


if __name__ == "__main__":
    ########### inica la conexión con el servidor ###########
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.connect((socket.gethostname(), 1234))
    #########################################################
    
    
    ########### Recibe la llave publica ###################
    key = int(server.recv(1024).decode())
    X0 = int(server.recv(1024).decode())
    print("public:", key)
    print("X0:",X0)
    
    ############ Encripta la data ###############
    file1 = open(r'.\resultados\bcrypthashed.txt', 'r') 
    Lines = file1.readlines()
    
    server.send('start'.encode())
    HEADERSIZE = 10
    for line in Lines:
        hash = line.strip() # elimina el \n
        encrypted = encrypt(hash, X0, key)
        msg = pickle.dumps(encrypted)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print(msg)
        server.send(msg)
        server.recv(1024)
        time.sleep(0.1)
    print('stop')
    # server.send('stop'.encode())
    # xd = server.recv(4096)
    print(datetime.datetime.now())
    
    
    
    
    # print(msg.decode("utf-8"))
    # msg_ret = 'holamundo'
    # time.sleep(5)
    # server.send(msg_ret.encode())
    # print("mensaje enviado")