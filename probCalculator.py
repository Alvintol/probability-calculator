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
      
      while numToDraw > 0:
        if len(contentsCopy) == 0:
          contentsCopy = copy(self.contents)
        
        index = randint(1, numToDraw)  
        print('INDEX:', index) 
        ballPulled = contentsCopy[index]
        pulledFromHat.append(ballPulled)
        contentsCopy.pop(index)
        numToDraw -= 1
      return pulledFromHat
    
# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#   expectedOutcome = 0
#   experimentsRan = 0
  
#   while experimentsRan <= num_experiments:
#     if ()
#     hat.draw(num_balls_drawn)
  
#   return expectedOutcome / num_experiments

    

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(5))