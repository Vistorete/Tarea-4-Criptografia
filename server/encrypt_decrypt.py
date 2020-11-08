import math
import random
from key_generator import jacobi

def convert(list):
	s = [str(i) for i in list]
	res = int("".join(s))
	return(res)

def int_to_bool_list(n):
	return [b == "1" for b in "{0:b}".format(n)]

def encrypt(data_dec, public_key):
	data_bin = int_to_bool_list(data_dec)
	n, y = public_key
	arr_encrypt = []

	for i in range(len(data_bin)):
		x = random.randint(0, n)
		if data_bin[i]:
			c = (y * pow(x, 2, n)) % n
			arr_encrypt.append(c)
		else:
			c = pow(x, 2, n)
			arr_encrypt.append(c)
	return arr_encrypt

def bool_list_to_int(n):
	s = ''.join(['1' if b else '0' for b in n])
	return int(s, 2)

def decrypt(arr_encrypt, private_key):
	p, q = private_key
	data_bin = []
	
	def decrypt_bit(c):
		e = jacobi(c, p)
		if e == 1:
			return False
		return True

	for i in range(len(arr_encrypt)):
		data_bin.append(decrypt_bit(arr_encrypt[i]))

	return bool_list_to_int(data_bin)    

def convert(num, base):
	buffer_list = []
	even = num
	while even != 0:
		residue = even % base
		even = even // base
		buffer_list.insert(0, residue)
	return buffer_list