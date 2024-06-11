import math
import random

height = 750
width = 750
cellSize = 15
row = int(height / cellSize)
column = int(width / cellSize)

class Food:
    def __init__(self, ):
        self.x = math.floor(random.random() * column + 1) * cellSize
        self.y = math.floor(random.random() * row + 1) * cellSize

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setNewLocation(self):
        new_x = math.floor(random.random() * (column - 2)) * cellSize
        new_y = math.floor(random.random() * (row - 2)) * cellSize

        self.x = new_x
        self.y = new_y
        return (self.x, self.y)

    def check_overlap(self, s):
        snake_body = s.getSnakebody()
        for j in range(0, len(s.getSnakebody())):
            if self.x == s.snake_body[0].getX() & self.y == snake_body[0].getY():
                return True
        return False

    def drawFruit(self, img, window):
        img.convert()
        window.blit(img, (self.x, self.y))
