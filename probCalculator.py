from random import randint

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, number in balls.items():
            for ball in range(number):
                self.contents.append(color)



Hat(yellow=3, blue=2, green=6)
Hat(red=5, orange=4)
Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
