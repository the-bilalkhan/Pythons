import random

class Dice:
        def roll(self):
                dots1 = (1, 2, 3, 4, 5, 6)
                dots2 = (1, 2, 3, 4, 5, 6)

                dot1 = random.choice(dots1)
                dot2 = random.choice(dots2)

                return f"({dot1},{dot2})"




newboard = Dice()

print(newboard.roll())