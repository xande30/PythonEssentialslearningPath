#demonstrating classes

from colorama import Fore

class Classy:
	def method(self, par):
		print(Fore.MAGENTA, "method: ", par)

obj = Classy()
obj.method(1)
obj.method(3)
