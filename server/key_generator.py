import string
from random import randint
from prime_generator import prime_generator
import sys
import functools 
import math

def is_even(x):
	return x % 2 == 0

def jacobi(a,p):
	nod = math.gcd(a,p)
	if nod == 1:
		power = (p-1)//2
		if pow(a, power, p) == 1:
			return 1
		else:
			return -1
	else:
		return 0

def quadratic_non_residue(p):
	a = 0
	while jacobi(a, p) != -1:
		a = randint(1, p)
	return a

def algExtendedEuclidean(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		nod, y, x = algExtendedEuclidean(b % a, a)
		return (nod, x - (b // a) * y, y)

def reverseElement(a, m):
	gcd, x, y = algExtendedEuclidean(a, m)
	if gcd != 1:
		return None
	else:
		return x % m

def gauss_crt(a, b, p, q):
	s1 = reverseElement(p,q) 
	s2 = reverseElement(q,p) 

	n = p * q

	c1 = (a * s1) % q 
	c2 = (b * s2) % p 

	result = (c1 * p + c2 * q) % n 
	return result

def pseudosquare(p, q):
	a = quadratic_non_residue(p)
	b = quadratic_non_residue(q)
	return gauss_crt(a, b, p, q)

def generate_key():
	p = prime_generator()
	q = prime_generator()

	while p == q:
		p = prime_generator()

	y = pseudosquare(p, q)
	n = p * q

	keys = {'public': (n, y), 'private': (p, q)}
	return keys  