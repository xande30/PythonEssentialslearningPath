#demonstrating memory buffer overflow

string = 'abcdefghijklmnoprstuvxyzABCDEFGHIJKLMNOPRSTUVXYZ'

try:
	while True:
		string = string + string
		print(len(string))
except MemoryError:
	print('This is not funny!')
