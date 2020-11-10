# hashcat.exe -m 0 -a 0 hash.txt wordlist.txt --force --outfile=prueba.txt
import os, datetime, time



def crack(hashed_words, dictionary, mode = 0):
    """
    mode = 0:       MD5
    mode = 10:      MD5 + Salt
    mode = 1000:    NTLM
    mode = 1800:    SHA-512
    """
    hashcat = r'E:\Users\Victor\Documents\GitHub\Tarea-4-Criptografia\hashcat-6.1.1\hashcat.exe'
    output = r'E:\Users\Victor\Documents\GitHub\Tarea-4-Criptografia\cracked_output.txt'
    cmd = '{} -m {} {} {}  --outfile={}'.format(hashcat, mode, hashed_words, dictionary, output)
    # mode, hash, dict
    os.system(cmd)
    pass


if __name__ == "__main__":
    palabras_hasheadas = r'E:\Users\Victor\Documents\GitHub\Tarea-4-Criptografia\ArchivoTarea4\Hashes\archivo_5'
    diccionario = r'E:\Users\Victor\Documents\GitHub\Tarea-4-Criptografia\ArchivoTarea4\diccionarios\diccionario_2.dict'
    
    start_time = datetime.datetime.now()
    crack(palabras_hasheadas, diccionario, mode = 1800)
    print(datetime.datetime.now() - start_time)
        
    




