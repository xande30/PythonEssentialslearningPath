from colorama import Fore


text = "Hello everybody this week we are releaseing the latest verison of our software.Please stay tunned and ready for a big change!"

fnd = text.find("tunned")
while fnd != -1:
	print(fnd)
	fnd = text.find("are", fnd +1)


