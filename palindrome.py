#is_palindrome = 'Eva can I stab bats in a cave'
#is_palindrome == lower(is_palindrome).reverse().is_palidrome[::-1]

phrase = input('Enter your phrase: ').lower()
clean = [letter for letter in phrase if letter.isalpha()]

if clean == clean[::-1]:
	print('This is palindrome')
else:
	print('This is not a palindrome')

