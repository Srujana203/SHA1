import numpy as np
import re

H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0


K1 = 0x5A827999         #( 0 <= t <= 19)
K2 = 0x6ED9EBA1         #(20 <= t <= 39)
K3 = 0x8F1BBCDC         #(40 <= t <= 59)
K4 = 0xCA62C1D6         #(60 <= t <= 79).


def function_f(t,B,C,D):
    if  0 <= t <= 19 :
        return (B and C) or ((not B) and D)
    elif 20 <= t <= 39:
        return B^C^D
    elif 40 <= t <= 59:
        return (B and C) or (B and D) or (C and D)
    else:
        return B^C^D

message = input('Please enter the message contents \n')
intial_message_length = len(message)

# Binary value of ASCII
binary_string = ''.join([bin(ord(num))[2:].zfill(8) for num in list(message)])

bits_length = len(binary_string)

# Append 1 to start padding
binary_string = binary_string +'1'

# Making the message congruent to 448 mod 512
while (len(binary_string) % 512 != 448):
    binary_string = binary_string + '0'

# Append length of binary representation in 64 bits
binary_string = binary_string + bin(bits_length)[2:].zfill(64)

# Spliting the binary string into 512 chunks
binary_string_chunks = re.findall('.{512}', binary_string)


#binary_message = hex(int(binary_string, base=2))
