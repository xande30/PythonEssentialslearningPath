#demonastrating classes and objects
from colorama import Fore

class Classy:
	pass


print(Fore.CYAN,Classy,__name__)
obj = Classy()

print(Fore.BLUE,type(obj).__name__)


