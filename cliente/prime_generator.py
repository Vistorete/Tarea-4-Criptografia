import random
import math

def generator():
    p_bin = []
    p_len = 50
    p_len = int(p_len)

    for i in range(p_len):
        rand_buf = random.randint(0, 1)
        p_bin.append(rand_buf)

    p_bin[0] = 1
    p_bin[p_len - 1] = 1
    p_bin_str = convert(p_bin)
    p_dec = int(str(p_bin_str), 2)

    return p_dec

def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)

prime_num_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,
          43,47,53,59,61,67,71,73,79,83,89,
          97,101,103,107,109,113,127,131,137,
          139,149,151,157,163,167,173,179,181,
          191,193,197,199,211,223,227,229,233,
          239,241,251]

def first_test(p_dec):
    i = 0
    bool = True
    while i < len(prime_num_list):
        if ((math.fmod(p_dec, prime_num_list[i]) != 0) or (p_dec == prime_num_list[i])):
            i += 1
            bool = True
        else:
            bool = False
            return bool
    return bool

def ferma_test(p_dec):
    j = 0
    bool = False
    while j < 5:
        rand_num = random.randint(1, p_dec - 1)
        nod = math.gcd(p_dec, rand_num)
        if nod != 1:
            j += 1
            bool = False
        else:
            if pow(rand_num, p_dec - 1, p_dec) == 1:
                j += 1
                bool = True
            else:
                j += 1
                bool = False
    return bool

def prime_generator():
    p_dec = generator()
    while first_test(p_dec) == False or ferma_test(p_dec) == False:
        p_dec = generator()
    return p_dec

