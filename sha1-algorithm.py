import numpy as np
import re

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
