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
        pulledFromHat = []

        if num > len(self.contents):
            return self.contents
        else:
            while numToDraw > 0:
                randomIndex = randint(0, len(self.contents) - 1)
                ballPulled = self.contents[randomIndex]
                pulledFromHat.append(ballPulled)
                self.contents.remove(self.contents[randomIndex])
                numToDraw -= 1

        return pulledFromHat


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expectedOutcome = 0
    experimentsRan = 0
    ballsDrawn = hat.draw(num_balls_drawn)
    ballsNeeded = [ball for ball in expected_balls]
    drawnTotal = {}

    for ball in ballsDrawn:
        if ball in drawnTotal:
            drawnTotal[ball] += 1
        else:
            drawnTotal[ball] = 1

    print('EXPECTEDBALLS:', expected_balls)
    print('BALLSDDRAWN:', ballsDrawn)
    print('BALLSNEEDED:', ballsNeeded)
    print('DDRAWNTOTAL:', drawnTotal)
    while experimentsRan <= num_experiments:
        #     neededTotals = {}
        experimentsRan += 1

    #     for total in drawnTotal:
    #         neededTotals[total] = drawnTotal[total]

        for ball, ballValue in expected_balls.items():
            # for drawn in drawnTotal.items():
            print('BALL:', ball)
            print('EXPECTED:', expected_balls[ball])
            print('DRAWN:', drawnTotal[ball])
            if ball not in drawnTotal.keys() or expected_balls[ball] <= drawnTotal[ball]:
                continue
        expectedOutcome += 1

    return expectedOutcome / num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(15))
