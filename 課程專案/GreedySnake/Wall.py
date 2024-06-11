import pygame.draw

white = (255, 255, 255)
height = 750
width = 750
cellSize = 15
row = int(height / cellSize)
column = int(width / cellSize)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Wall:

    def __init__(self):
        self.wall_body = []
        for i in range(0, row):
            self.wall_body.append(Node(0, i * cellSize))
            self.wall_body.append(Node(width - cellSize, i * cellSize))
        for j in range(1, column - 1):
            self.wall_body.append(Node(j * cellSize, 0))
            self.wall_body.append(Node(j * cellSize, height - cellSize))

    def getWallbody(self):

        return self.wall_body

    def drawWall(self, window):

        for i in range(0, len(self.wall_body)):
            n = self.wall_body[i]
            pygame.draw.rect(window, white, (n.x, n.y, cellSize, cellSize))

    def check_overlap(self, head):
        wall = self.getWallbody()
        for j in range(1, len(wall)):
            if wall[j].x == head.getX() and wall[j].y == head.getY():
                return True
        return False
