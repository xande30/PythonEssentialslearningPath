#demomstrating lists easily

from colorama import Fore


my_list = [1 if x % 2 == 0 else 0 for x in range (14)]
print(Fore.MAGENTA, my_list)
