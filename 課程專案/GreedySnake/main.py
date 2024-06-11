import pygame
import sys
import Food
import Snake
import time
import Wall
import Scores

pygame.init()
pygame.font.init()

# 設定遊戲視窗大小
height, width = 750, 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Greedy Snake")  # 設定視窗名稱

# 遊戲初始化設定
cellSize = 15
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
gray = (200, 200, 200)
fruitImg = pygame.image.load("./fruit.png")

# 遊戲部份
running = True
snake = Snake.Snake()
food = Food.Food()
wall = Wall.Wall()
scoreM = Scores.ScoreManager("/Users/Lawrence/Downloads/scores.txt")
direction = "right"
overlapping = False
point = 0
diff = 10
name = ""


def input_name_screen():
    clock = pygame.time.Clock()
    input_box = pygame.Rect(150, 300, 450, 50)
    color_inactive = gray
    color_active = black
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        font_path = pygame.font.get_default_font()  # 使用默認字體
        font = pygame.font.Font(font_path, 30)
        input_font = pygame.font.Font(font_path, 20)

        window.fill(white)
        draw_text("Enter your name", font, black, window, width // 2, height / 3)
        # Render the current text.
        txt_surface = input_font.render(text, True, color)
        # Resize the box if the text is too long.
        width_txt = max(400, txt_surface.get_width() + 10)
        input_box.w = width_txt
        # Blit the text.
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(window, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


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
    rank_font = pygame.font.Font(font_path, 15)
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
    global point

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 500, 100)
        self.color = OverWindow.white

    def draw(self, surface, point):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(f"You got {point} point", OverWindow.label_font, OverWindow.black, window, self.rect.centerx,
                  self.rect.centery)

    def showRank(self, surface, text):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(text, OverWindow.label_font, OverWindow.black, window, self.rect.centerx, self.rect.centery)


class Rank:
    global point

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 250, 20)
        self.color = OverWindow.white

    def showRank(self, surface, text):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(text, OverWindow.rank_font, OverWindow.black, window, self.rect.centerx, self.rect.centery)


def over_window():
    global point

    pygame.display.set_caption("Game Over")  # 設定視窗名稱

    # 創建按鈕實例
    label = Label((width / 6), 200)
    rank1 = Rank((width / 3), 300)
    rank2 = Rank((width / 3), 320)
    rank3 = Rank((width / 3), 340)
    rank4 = Rank((width / 3), 360)
    rank5 = Rank((width / 3), 400)
    rank = [rank1, rank2, rank3, rank4, rank5]
    restart_button = Button("Restart", (width / 5), 500, (width / 5), 80, on_restart)
    quit_button = Button("Quit", 3 * (width / 5), 500, (width / 5), 80, on_quit)

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
        label.draw(window, point)
        text_list = scoreM.get_top_five_scores(5)
        if (len(text_list)) >= 5:
            limit = 5
        else:
            limit = len(text_list)
        for i in range(0, limit):
            rank[i].showRank(window, str(text_list[i]))

        pygame.display.flip()


# 按鈕回調函數
def on_restart():
    global snake, food, direction, point, running
    print("重新開始")
    scoreM.add_score(name, point)

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
    scoreM.add_score(name, point)
    pygame.quit()
    sys.exit()


def main_game_loop():
    global running, snake, food, direction, point, allowKeypress, diff, name

    pygame.display.set_caption("Greedy Snake")

    name = input_name_screen()
    print(f"Player name: {name}")

    while running:

        if point % 10 == 0 and point != 0:
            diff *= 0.8

        # 將畫布填滿黑色
        window.fill(black)

        # 蛇的移動
        last = snake.move(direction)
        time.sleep(diff / 100)

        # 確認是否 Overlap
        if snake.getSnakebody()[0].x == food.getX() and snake.getSnakebody()[0].y == food.getY():
            food.setNewLocation()
            point += 1
            snake.snake_body.append(last)
        if snake.check_overlap(snake.getSnakebody()[0]) or wall.check_overlap(snake.getSnakebody()[0]):
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

        # 畫出蛇與水果
        food.drawFruit(fruitImg, window)
        snake.drawSnake(window)
        wall.drawWall(window)
        allowKeypress = True

        pygame.display.flip()


main_game_loop()
