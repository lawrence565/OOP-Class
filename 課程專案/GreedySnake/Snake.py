import pygame.draw

yellow = (255, 215, 0)
orange = (255, 69, 0)
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


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_body.append(Node(60, 30))
        self.snake_body.append(Node(45, 30))
        self.snake_body.append(Node(30, 30))
        self.snake_body.append(Node(15, 30))

    def getSnakebody(self):
        return self.snake_body

    def drawSnake(self, window):

        for i in range(0, len(self.snake_body)):
            n = self.snake_body[i]
            if i == 0:  # 蛇頭選藍色
                color = orange
            else:
                color = yellow
            if n.x >= width:
                n.x = 0
            if n.x < 0:
                n.x = width - cellSize
            if n.y >= height:
                n.y = 0
            if n.y < 0:
                n.y = height - cellSize

            pygame.draw.rect(window, color, (n.x, n.y, cellSize, cellSize))

    def move(self, direction):
        snake = self.snake_body
        x = snake[0].getX()
        y = snake[0].getY()
        if direction == "right":
            if x == width:
                new_head = Node(0, y)
            else:
                new_head = Node(x + cellSize, y)
            snake.insert(0, new_head)
            last = snake.pop()
        elif direction == "up":
            new_head = Node(x, y - cellSize)
            snake.insert(0, new_head)
            last = snake.pop()
        elif direction == "left":
            new_head = Node(x - cellSize, y)
            snake.insert(0, new_head)
            last = snake.pop()
        elif direction == "down":
            new_head = Node(x, y + cellSize)
            snake.insert(0, new_head)
            last = snake.pop()
        return last

    def check_overlap(self, head):
        snake_body = self.getSnakebody()
        for j in range(1, len(snake_body)):
            if snake_body[j].x == head.getX() and snake_body[j].y == head.getY():
                return True
        return False
