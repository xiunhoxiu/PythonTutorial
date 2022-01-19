import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # return in a tuple


dice = Dice()
print(dice.roll())