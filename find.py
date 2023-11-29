#demonstrating the find method

from colorama import Fore
print("""
	0:00 Catch Me If You Can (2002)
	2:12 Groundhog Day (1993)
	3:39 Limitless (2011)
	5:36 Fight Club (1999)
	8:06 The Way Way Back (2013)
	The Count of Monte Cristo 
	12:30 Crazy Stupid Love (2011)
	15:14 Elf (2003)""".find("Can"))

print(Fore.GREEN,"Can".find("Club"))

my_movie = input("What is your beloved movie from the ones listed above? ")
if my_movie !=  "The Count of Monte Cristo":
	print(Fore.BLUE,"I love this movie!")
else:
	pass
