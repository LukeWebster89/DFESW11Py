#use a dice class to generate random dice rolls

import random

class Dice():

    def dice_d6():
        return random.randint(1,6)
    
    def dice_d2():
        return random.randint(1,2)

    def dice_d20():
        return random.randint(1,20)

    def dice_d4():
        return random.randint(1,4)    


for i in range(0,4):
    print(Dice.dice_d6(), end = " ")
