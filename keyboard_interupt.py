#demonastrating how the exception keyboard interrupt functions

from time import sleep

seconds = 0

while True:
	try:
		print(seconds)
		seconds += 1
		sleep(1)
	except KeyboardInterrupt:
		print("Continue!:")
		text = 'Continue'
		if text == "Continue":
			print("Stop!")
		else:
			break
