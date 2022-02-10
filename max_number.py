#Write a Python function to find the Max of three numbers.

def max_number(num1, num2, num3):
    if num1 > num2 and num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


print (max_number(1,3,4))

