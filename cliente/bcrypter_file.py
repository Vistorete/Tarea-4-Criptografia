import bcrypt
import codecs
import os, datetime, time

def gen_hash_from_file(path_file, salt = bcrypt.gensalt(), writer = None):
    file1 = open(path_file, 'r') 
    Lines = file1.readlines()
    for line in Lines:
        word_list = line.split(":")
        word_list[-1] = word_list[-1].strip()
        passwd = word_list[-1].encode('utf-8')
        hashed = bcrypt.hashpw(passwd, salt)
        if writer:
            writer.write(hashed.decode()+'\n')
    pass

if __name__ == "__main__":
    # salt = bcrypt.gensalt(rounds=5)
    start_time = datetime.datetime.now() # tiempo inicial
    salt = bcrypt.gensalt()
    with open(r'.\resultados\bcrypthashed.txt','w') as f: # en donde se quiere guardar el archivo
        gen_hash_from_file(r'.\resultados\cracked_output1.txt', salt, f)
        gen_hash_from_file(r'.\resultados\cracked_output2.txt', salt, f)
        gen_hash_from_file(r'.\resultados\cracked_output3.txt', salt, f)
        gen_hash_from_file(r'.\resultados\cracked_output4.txt', salt, f)
        gen_hash_from_file(r'.\resultados\cracked_output5.txt', salt, f)

    print(datetime.datetime.now() - start_time)
    pass
    

# hex_hash = hashed.hex()
# utf8_hash = codecs.decode(hex_hash, "hex").decode('utf-8')

# print(utf8_hash)
# print(hex_hash)
# gm_word = hex_to_gm_format(hex_hash)
# print(gm_word)
# print(gm_format_to_hex(gm_word))



