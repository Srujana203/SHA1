
message = input('Please enter the message contents \n')
intial_message_length = len(message)


# ASCII values of characters
message = list(map(ord, list(message)))

# Binary values of ASCII to String
binary_message = ''.join([bin(num)[2:].zfill(8) for num in message])

