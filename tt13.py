#demonstrating classes and its inheritance  #01

from colorama import Fore

class Vehicle:
	pass

class LandVehicle(Vehicle):
	pass

class TrackedVehicle(LandVehicle):
	pass


for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
	for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
		print(Fore.CYAN, issubclass(cls1,cls2), end="\t")
	print()
