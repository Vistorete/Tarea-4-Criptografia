import socket
from prime_generator import prime_generator
import random
import math
import sys
from BG import public_key_generation, encrypt, decrypt, bin_toAscii
import time
import datetime
import sqlite3, os
import pickle

DB_PATH = r'.\sqlite-tools-win32-x86-3330000\database.db'

table_statement = '''CREATE TABLE IF NOT EXISTS hashes(
                        id integer PRIMARY KEY,
                        hash_ascii text NOT NULL); '''                        

table_delete = '''DROP TABLE hashes;'''


    
             
if __name__ == "__main__":
    #### Conexion a la BD #############
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    if db:
        cursor.execute(table_delete)
        cursor.execute(table_statement)


    
    ####################################
    
    ########### Inicia el servidor ###########
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen(5)
    
    cliente, direccion = s.accept() # obtiene la conexion con cliente
    print(f'Se ha establecido conexion desde {direccion}')
    ############################################
    
    
    
    ########### Envia la llave publica ###################
    #(p,q) Private key
    # p = prime_generator()
    # q = prime_generator()
    p = 499  
    q = 547
    X0 = 159201
    public_key = public_key_generation(p,q)
    
    cliente.send(str(public_key).encode())
    cliente.send(str(X0).encode())
    
    print("Listo para enviar llave publica")


    ############################################
    
    ########### Recibe la data encriptada ###################
    print(cliente.recv(1024).decode()) # Recibe 'start'
    HEADERSIZE = 10
    full_msg = b''
    new_msg = True
    table_id = 0
    try:
        
        while True:
            msg = cliente.recv(4096)
            if new_msg:
                # print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            # print(f"full message length: {msglen}")

            full_msg += msg

            # print(len(full_msg))
            
            if len(full_msg)-HEADERSIZE == msglen:
                # print("full msg recvd")
                # print(full_msg[HEADERSIZE:])
                encrypted = pickle.loads(full_msg[HEADERSIZE:])
                print("mensaje cifrado:", encrypted)
                decrypted = decrypt(p,q,encrypted)
                print("mensaje descifrado (ASCII):",bin_toAscii(decrypted))
                new_msg = True
                full_msg = b""
                table_insert = f'INSERT INTO hashes (id, hash_ascii) VALUES ({table_id}, \'{bin_toAscii(decrypted)}\');'
                
                cursor.execute(table_insert)
                db.commit()
                table_id += 1
                cliente.send("ok".encode())
                ############# Almacena el mensaje desencriptado en ######
    except:
        db.close()
        print(f"total elementos insertaods {table_id + 1}")
    
