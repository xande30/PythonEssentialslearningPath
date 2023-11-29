#demonstrating iban validator
from colorama import Fore

iban = input("ENTER YOUR <IBAN> PLEASE: ")
iban = iban.replace(' ','')

if not iban.isalnum():
	print(Fore.RED,"YOU PROVIDED AN INVALID IBAN NUMBER!")
elif len(iban) < 15:
	print(Fore.RED,"IBAN ENTERED IS TOO SHORT!")
elif len(iban) > 31:
	print(Fore.RED,"IBAN IS TOO LONG!")
else:
	iban = (iban[4:] + iban[0:4]).upper()
	iban2 = ''
	print(Fore.BLUE, "YOUR INPUT MATCH WITH OUR IBAN FROM THE BANKS DATABASE.CONGRATULATIONS!")
