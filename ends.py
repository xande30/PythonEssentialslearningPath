#demosntrating endswith method

from colorama import Fore

if "sigma_tellicon".endswith("on"):
	print(Fore.CYAN, "Yes It's True!")
else:
	print(Fore.RED, "NO!")
