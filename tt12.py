#demonstrating classes and its inheritance

from colorama import Fore

class Star:
	def __init__(self, name, galaxy):
		self.name = name
		self.galaxy = galaxy


sun = Star('Sun', 'Tzu')
print(Fore.CYAN,sun)
