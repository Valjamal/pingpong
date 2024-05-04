from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width , win_height))
display.set_caption("PingPong")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

speed_x = 5
speed_y = 5

player1 = Player('Ems.jpg', 5, win_height - 100, 50, 150, 10)

player2 = Enemy('Ims.jpg', 5, win_height - 100, 50, 150, 10)

ball = GameSprite('ball.jpg', 5, win_height - 100, 50, 50, 10)

font.init()
font1 = font.SysFont('Arial', 80)
lose1 = font1.render('1 - проиграл!', True, (255, 255, 255))
lose2 = font1.render('2 - проиграл!', True, (180, 0, 0))

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player1.update()
        player2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x < 650:
            finish = True
            window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)

