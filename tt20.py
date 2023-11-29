#demonstrating lambda expression

from colorama import Fore

print(Fore.LIGHTGREEN_EX,"THE MATRIX :)")
x = 2
y = 3
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x,y: x ** y
to = lambda x,y: x % y
the = lambda x,y: x * y
people = lambda x,y : x + y
for a in range(-2,3):
	print(Fore.RED,sqr(a), end=" ", sep="\n")
	print(Fore.YELLOW,pwr(a, two()))
	print(Fore.BLUE,to(y,y))
	print(Fore.GREEN,the(y,y))
	print(Fore.CYAN, people(y,y))
