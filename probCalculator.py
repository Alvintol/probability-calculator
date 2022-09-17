import random
import copy
from random import randint
from copy import copy


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, number in balls.items():
            for ball in range(number):
                self.contents.append(color)

    def draw(self, num):
        numToDraw = num
        contentsCopy = copy(self.contents)
        pulledFromHat = []
        drawnTotal = {}

        if num > len(contentsCopy):
            return self.contents
        else:
            while len(contentsCopy) >= num:
                index = randint(0, len(contentsCopy) - 1)
                ballPulled = contentsCopy[index]
                pulledFromHat.append(ballPulled)
                contentsCopy.remove(contentsCopy[index])
                numToDraw -= 1

                for ball in pulledFromHat:
                    if ball in drawnTotal:
                        drawnTotal[ball] += 1
                    else:
                        drawnTotal[ball] = 1

        print('PULLEDFROMHAT:', [ball for ball in drawnTotal])
        print('PULLEDFROMHAT:', pulledFromHat)
        return [ball for ball in drawnTotal]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expectedOutcome = 0
    experimentsRan = 0
    ballsNeeded = []

    ballsNeeded = [ball for ball in expected_balls]

    # while experimentsRan <= num_experiments:
    #     ballsDrawn = hat.draw(num_balls_drawn)
    #     # neededTotals = {}
    #     experimentsRan += 1

    #     # for total in drawnTotal:
    #     #     neededTotals[total] = drawnTotal[total]

    #     # for item, value in neededTotals.items():

    #     #     print('ITEM:', item, value)

    #     # for ball, ballValue in expected_balls.items():
    #     #     for drawn, drawnValue in drawnTotal.items():
    #     #         if drawnValue <= ballValue:
    #     #             continue

    #     expectedOutcome += 1

    #     # print('BALLSNEEDED:', ballsNeeded)
    #     # print('EXPECTEDBALLS:', expected_balls)
    #     # print('DDRAWNTOTAL:', drawnTotal)

    return expectedOutcome / num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(15))
