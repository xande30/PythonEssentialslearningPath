#demonatrating classes and methods

from colorama import Fore

class Classy:
	my_check = 100000
	def method(self):
		print(Fore.MAGENTA, self.my_check,self.var)


obj = Classy()
obj.var = 1000000
obj.method()
