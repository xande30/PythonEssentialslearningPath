#demonstrating exceptions 01

from math import tan, radians

angle = int(input('Enter integral angle in degrees: '))

assert angle % 100 != 90
print(tan(radians(angle)))
