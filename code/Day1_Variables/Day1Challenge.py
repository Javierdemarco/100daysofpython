#####
# Day 1 Challeges
#
#####
import numpy as np
# Day 1 - 1: Printing
print("Day 1 - Python Print Function")
print("The functio is declared like this:")
print("print('What to print')\n")
# Day 1 - 2 - Fix error
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n")
# Day 1 - 3: Length of input
print(len(input("What is your name?\n")))
# Day 1 - 4: Switch number values
a = int(input("a: "))
b = int(input("b: "))
a = a+b
b = a-b  # b = a / a = a+b(antiguo)
a = a-b  # only works on numbers
print("a: " + str(a))
print("b: " + str(b))
