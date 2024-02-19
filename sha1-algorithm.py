
message = input('Please enter the message contents \n')
intial_message_length = len(message)

# Binary value of ASCII
binary_message = hex(int(''.join([bin(ord(num))[2:].zfill(8) for num in list(message)]), base=2))
