#iterating  through a string
from colorama import Fore

my_string = "TheMatrix"

for character in my_string:
	print(Fore.CYAN, character, end=' ', sep='#')

print(Fore.CYAN, 'We love colours!')


print(my_string)


#demonstrating max() function 

print(max("aAbByZXXdjfjf"))

t = 'The Dark Night'
print('[' + max(t) + ']')

t = [0,1,2]
print(max(t))
