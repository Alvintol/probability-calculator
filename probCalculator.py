from random import randint
from copy import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, number in balls.items():
            for ball in range(number):
                self.contents.append(color)

    def draw(self, num):
      ballsToDraw = num
      contentsCopy = copy(self.contents)
      
      return

Hat(yellow=3, blue=2, green=6)
Hat(red=5, orange=4)
Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
