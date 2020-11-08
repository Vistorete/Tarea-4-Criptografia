from key_generator import *
from encrypt_decrypt import *
import random
import math
import sys	

key = generate_key()
print('КЛЮЧ: ', key)

data_in = 'hola muñndo1'

data = data_in.upper()
print('ИСХОДНЫЕ ДАННЫЕ: ', data)

data_dec = 0
data_list_ord = []

for i in range(len(data)):
	ind = ord(data[i]) 
	if ord('A') <= ind <= ord('Z'):
		val = ind - ord('A') + 1
	else: 
		val = 0
	data_dec += val * pow(27, len(data) - 1 - i)
	data_list_ord.append(val)	

print(data_dec)

encryp = encrypt(data_dec, key['public'])
print('ЗАШИФРОВАННЫЕ ДАННЫЕ:', encryp)

data_encryp = open('./data/encrypt.txt', 'w')

data_encryp.write(str(encryp)) 
data_encryp.close()

decryp = decrypt(encryp, key['private'])
while decryp != data_dec:
	key = generate_key()
	encryp = encrypt(data_dec, key['public'])
	decryp = decrypt(encryp, key['private'])

print('ДАННЫЕ ПОСЛЕ РАСШИФРОВКИ:', decryp)
		
data_convert =convert(data_dec, 27)
data_list_char = []

for i in range(len(data_convert)):
	if data_convert[i] == 0:
		char = chr(32)
	else: 
		char = chr(data_convert[i] + ord('A') - 1)
	data_list_char.append(char)
	
print('РАСШИФРОВАННЫЕ ДАННЫЕ: ', data_list_char)

data_output = open('./data/output.txt', 'w')

for i in range(len(data_list_char)):
	data_output.write(data_list_char[i]) 
data_output.close()