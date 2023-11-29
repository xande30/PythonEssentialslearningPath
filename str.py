#indexing strings

from colorama import Fore

my_string = 'the matrix'

for ix in range(len(my_string)):
	print(Fore.CYAN,my_string[ix], end='', sep='#')

print(Fore.BLUE, "We printed successfully our string!")
