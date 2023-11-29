#demonatrating an analyse on how classes work in python

from colorama import Fore
class Super:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "My Name is  : " + self.name


def Sub(Super):
	def __init__(slef,name):
		Super.__init__(self,name)

obj = "Cyan"
print(Fore.MAGENTA, obj)
