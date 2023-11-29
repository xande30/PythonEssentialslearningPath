#demonstrating list comprehensions

from colorama import Fore

list_1 = []

for nr in range(13):
	list_1.append(10 ** nr)

list_2 = [10 ** nr for nr in range(13)]

print(Fore.BLUE,list_1,list_2)
print(Fore.MAGENTA, "Our List Has Been Successfully Populated!")
