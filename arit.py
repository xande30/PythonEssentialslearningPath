#demonstrating exceptions

try:
	y = 1 / 0
except ArithmeticError:
	print("Error!")
print("The End!")
