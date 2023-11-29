#demonstrating classes and modules

from colorama import Fore

class Sample:
	def __init__(self):
		self.name = Sample.__name__
	def myself(self):
		print(Fore.CYAN, "My Name Is " + self.name + " Living in a " + Sample.__module__)

obj = Sample()
obj.myself()

print(Fore.MAGENTA, "Our Class Was Performed Succcessfully!Hurra!")

