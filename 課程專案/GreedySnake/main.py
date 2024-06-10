import pygame
import sys
import Food
import Snake
import time

pygame.init()
pygame.font.init()

# 設定遊戲視窗大小
height, width = 720, 1280
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Greedy Snake")  # 設定視窗名稱

# 遊戲初始化設定
cellSize = 20
row = int(height / cellSize)
column = int(width / cellSize)
allowKeypress = True

# 顏色初始化設定
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 69, 0)
fruitImg = pygame.image.load("./fruit.png")

# 遊戲部份
running = True
snake = Snake.Snake()
food = Food.Food()
direction = "right"
overlapping = False
point = 0


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


class OverWindow:
    # 設置顏色
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (200, 200, 200)
    blue = (0, 0, 255)

    # 字體設定
    font_path = pygame.font.get_default_font()  # 使用默認字體
    label_font = pygame.font.Font(font_path, 55)
    button_font = pygame.font.Font(font_path, 30)

    def __init__(self):
        self.width, self.height = 640, 360
        pygame.display.set_caption("Game Over!")


class Button:
    def __init__(self, text, x, y, width, height, callback, border_radius=10):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = OverWindow.gray
        self.callback = callback
        self.border_radius = border_radius

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.border_radius)
        draw_text(self.text, OverWindow.button_font, OverWindow.black, window, self.rect.centerx, self.rect.centery)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


class Label:
    def __init__(self, x, y, point):
        self.text = f"You got {point} point"
        self.rect = pygame.Rect(x, y, 500, 100)
        self.color = OverWindow.white

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, OverWindow.label_font, OverWindow.black, window, self.rect.centerx, self.rect.centery)


def over_window():
    global point

    pygame.display.set_caption("Game Over")  # 設定視窗名稱

    # 創建按鈕實例
    label = Label(380, 200, point)
    restart_button = Button("Restart", 256, 400, 256, 80, on_restart)
    quit_button = Button("Quit", 768, 400, 256, 80, on_quit)

    buttons = [restart_button, quit_button]

    # 主循環
    over = True
    while over:
        window.fill(OverWindow.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for button in buttons:
                button.handle_event(event)

        for button in buttons:
            button.draw(window)
        label.draw(window)

        pygame.display.flip()


# 按鈕回調函數
def on_restart():
    global snake, food, direction, point, running
    print("重新開始")

    # 重新設置全域變數
    snake = Snake.Snake()
    food = Food.Food()
    direction = "right"
    point = 0
    running = True

    # 回到主遊戲循環
    main_game_loop()


def on_quit():
    print("離開遊戲")
    pygame.quit()
    sys.exit()


def main_game_loop():
    global running, snake, food, direction, point, allowKeypress

    pygame.display.set_caption("Greedy Snake")

    while running:

        # 將畫布填滿黑色
        window.fill(black)

        # 畫出蛇與水果
        food.drawFruit(fruitImg, window)
        snake.drawSnake(window)
        allowKeypress = True

        # 蛇的移動
        last = snake.move(direction)
        time.sleep(0.1)

        # 確認是否 Overlap
        if snake.getSnakebody()[0].x == food.getX() and snake.getSnakebody()[0].y == food.getY():
            food.setNewLocation()
            point += 1
            snake.snake_body.append(last)
        if snake.check_overlap(snake.getSnakebody()[0]):
            running = False
            over_window()

        # 偵測事件
        for event in pygame.event.get():

            # 偵測使用者鍵盤
            if event.type == pygame.KEYDOWN and allowKeypress:
                if event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                elif event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
            allowKeypress = False

            # 關閉視窗後離開主迴圈
            if event.type == pygame.QUIT:
                running = False
                over_window()

        pygame.display.flip()


main_game_loop()
