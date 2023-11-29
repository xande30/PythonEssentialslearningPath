#demonstrating classes and methods

from colorama import Fore

class Classy:
	def other(self):
		print(Fore.MAGENTA,"other")
	def method(self):
		print(Fore.YELLOW,"method")
		self.other()


obj = Classy()
obj.method()
