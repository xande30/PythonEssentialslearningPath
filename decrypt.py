#decrypting caesar ciper 

from colorama import Fore

cipher = input("Enter your cryptogram: ")
text = ""

for char in cipher:
	if not char.isalpha():
		continue
	char = char.upper()
	code = ord(char) -1
	if code < ord('A'):
		code = ord('Z')
	text += chr(code)

print(Fore.MAGENTA, text)
