
#demonstrating classes and its inheritances 

from colorama import Fore,Back
class SuperHero:
	pass

class SuperCars:
	pass

class Sub(SuperHero, SuperCars):
	pass

def printBases(cls):
	print('[',end='', sep='$'']')

	for x in cls.__bases__:
		print(Fore.LIGHTCYAN_EX, x.__name__, end='', sep='$')

print(Fore.RED,printBases(SuperHero))
print(Fore.YELLOW,printBases(SuperCars))
print(Fore.BLUE,printBases(Sub))
