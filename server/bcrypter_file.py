import bcrypt
import codecs
import os, datetime, time

def gen_hash_from_file(path_file, salt = bcrypt.gensalt()):
    file1 = open(path_file, 'r') 
    Lines = file1.readlines()
    for line in Lines:
        word_list = line.split(":")
        word_list[-1] = word_list[-1].strip()
        passwd = word_list[-1].encode('utf-8')
        hashed = bcrypt.hashpw(passwd, salt)
        print(hashed)
    pass

def hex_to_gm_format(hex_word):
    hex_word = hex_word.replace("0", "g")
    hex_word = hex_word.replace("1", "h")
    hex_word = hex_word.replace("2", "i")
    hex_word = hex_word.replace("3", "j")
    hex_word = hex_word.replace("4", "k")
    hex_word = hex_word.replace("5", "l")
    hex_word = hex_word.replace("6", "m")
    hex_word = hex_word.replace("7", "n")
    hex_word = hex_word.replace("8", "o")
    hex_word = hex_word.replace("9", "p")

    return hex_word

def gm_format_to_hex(gm_word):
    gm_word = gm_word.replace("g", "0")
    gm_word = gm_word.replace("h", "1")
    gm_word = gm_word.replace("i", "2")
    gm_word = gm_word.replace("j", "3")
    gm_word = gm_word.replace("k", "4")
    gm_word = gm_word.replace("l", "5")
    gm_word = gm_word.replace("m", "6")
    gm_word = gm_word.replace("n", "7")
    gm_word = gm_word.replace("o", "8")
    gm_word = gm_word.replace("p", "9")
    
    return gm_word
     



if __name__ == "__main__":
    # salt = bcrypt.gensalt(rounds=5)
    start_time = datetime.datetime.now()
    salt = bcrypt.gensalt()
    gen_hash_from_file(r'.\resultados\cracked_output1.txt', salt)
    gen_hash_from_file(r'.\resultados\cracked_output2.txt', salt)
    gen_hash_from_file(r'.\resultados\cracked_output3.txt', salt)
    gen_hash_from_file(r'.\resultados\cracked_output4.txt', salt)
    gen_hash_from_file(r'.\resultados\cracked_output5.txt', salt)
    print(datetime.datetime.now() - start_time)
    pass
    

# hex_hash = hashed.hex()
# utf8_hash = codecs.decode(hex_hash, "hex").decode('utf-8')

# print(utf8_hash)
# print(hex_hash)
# gm_word = hex_to_gm_format(hex_hash)
# print(gm_word)
# print(gm_format_to_hex(gm_word))



