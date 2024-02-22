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
    result = 0x00000000
    if  0 <= t <= 19 :
        result = (B & C) | ((not B) & D)
        return result + K1
    elif 20 <= t <= 39:
        result = B^C^D
        return result + K2
    elif 40 <= t <= 59:
        result = (B & C) | (B & D) | (C & D)
        return result + K3
    else:
        result = B^C^D
        return result + K4

def rol32(a,n):
	return ((a << n) | (a >> (32 - n))) & 0xffffffff # Ensures 32-bit

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

for message_chunk in binary_string_chunks:
    
    # divide message_chunk into 16 32bit words
    message_chunk_list = list(map(lambda x: rol32(int(x,2),0),re.findall('.{32}',message_chunk)))

    # perform message schedule for 16-79 words
    for i in range(80):
        message_chunk_list.append(rol32(message_chunk_list[i-3] ^ message_chunk_list[i-8] ^ message_chunk_list[i-14] ^ message_chunk_list[i-16],1))
    
    A = H0
    B = H1
    C = H2
    D = H3
    E = H4


    for t in range(0,80):
        #message_chunk_hex_value = hex_value(message_chunk_list[t])
        temp = rol32(A,5) + function_f(t,B,C,D) + E + message_chunk_list[t] & 0xffffffff
        E = D
        D = C
        C = rol32(B,30)
        B = A
        A = temp
    
    H0 = (H0 + A) & 0xffffffff
    H1 = (H1 + B) & 0xffffffff
    H2 = (H2 + C) & 0xffffffff
    H3 = (H3 + D) & 0xffffffff
    H4 = (H4 + E) & 0xffffffff

print('The final hash value of the input string is', '%08x%08x%08x%08x%08x' % (H0, H1, H2, H3, H4))
