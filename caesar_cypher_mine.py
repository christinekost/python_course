from string import ascii_lowercase


def encode(message, shift):
	alpha = ascii_lowercase
	shifted = alpha[shift:] + alpha[:shift]
	encoder = dict(zip(alpha, shifted))
	encoded_message = []
	for letter in message:
		encoded_message.append(encoder.get(letter, letter))
	return ''.join(encoded_message)

def decode(message, shift):
	return encode(message, -shift)

print(encode('Ozzy', 20))

print(decode(encode('Ozzy fhldh', 4), 4))
