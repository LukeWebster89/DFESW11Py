# Write a Python function to multiply all the numbers in a list.

#def multiply_all_numbers(number_input):
#    total = 1
#    for i in number_input:
#        total *= i
#    return total
# 
#print(multiply_all_numbers((3, 1, 3, 2)))

import math

def multiply_all_numbers(number_input):
    return math.prod(number_input)

print(multiply_all_numbers((1,2,3)))