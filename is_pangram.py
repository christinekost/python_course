from string import ascii_lowercase

phrase = input('Enter your phrase: ').lower()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# is_pangram = 'The quick brown fox jumps over the lazy dog'

if set(phrase).issuperset(set(ascii_lowercase)):
	print('Its really a pangram')
else:
	print('Its not pangram')
abc + 1