#analyzing classes 

from colorama import Fore, Back

class MyClass:
	pass

obj = MyClass()
obj.a = 7
obj.b = 5
obj.c = 1

obj.ireal = 14
obj.integer = 13
obj.z = 5

def inIntsI(obj):
	for name in obj.__dict__.keys():
		if name.startswith('i'):
			val = getattr(obj, name)
			if isinstance(val, int):
				setattr(obj, name, val + 1)

print(Fore.LIGHTMAGENTA_EX, obj.__dict__)
print(Fore.LIGHTMAGENTA_EX,inIntsI(obj))
print(Fore.LIGHTMAGENTA_EX, obj.__dict__)

