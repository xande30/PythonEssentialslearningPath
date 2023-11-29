#demonstrating how to elegantly leave a loop

list = [1,2,3,4]
ix = 0
do_it = True

while do_it:
	try:
		print(list[ix])
		ix += 1
	except IndexError:
		do_it = False

print('Done')
