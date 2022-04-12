
from time import sleep
import pygame
import random
from random import choice
pygame.init()

FPS = 60
WIDTH, HEIGHT = 400, 600
step = 5
#enemy_step = 10

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

score = 0 #счетчик для подсчета пройденных машин
score_coins = 0 # счетчик денег

#шрифты
font = pygame.font.SysFont("Verdana", 20)
font1 = pygame.font.SysFont("Verdana", 60)
game_over = font1.render("Game Over", True, BLACK)

# экран и название окошка
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars")

#задний фон
background = pygame.image.load('./images/bkg.png')
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 5

#звуки
sound = pygame.mixer.Sound("./music_cars/dollar.wav")
sound1 = pygame.mixer.Sound("./music_cars/crush.mp3")

#изображения монеток
coin1 = pygame.image.load('./images/dollar.png') #1
coin2 = pygame.image.load('./images/dollar-symbol.png') #3
coin3 = pygame.image.load('./images/money.png') #5
coin4 = pygame.image.load('./images/money-bag.png') #10

#лист монеток
money = [coin1, coin2, coin3, coin4]


class Player(pygame.sprite.Sprite): # класс игрока
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def update(self): #движение машинки 
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0: 
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-step, 0)
        if self.rect.right < WIDTH: 
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(step, 0)
        if self.rect.top > 0: 
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -step)
        if self.rect.bottom < HEIGHT: 
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, step)
    def draw(self, surface): # отрисовка
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite): # класс противников 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40 ),0)
        self.enemy_step = 10
    
    def update(self): #движение 
        global score
        self.rect.move_ip(0, self.enemy_step)
        if self.rect.bottom > HEIGHT:
            score += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface): #отрисовка
        surface.blit(self.image, self.rect)

class Coins(pygame.sprite.Sprite): # класс монеток
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24,WIDTH - 24), random.randint(24 ,HEIGHT - 24))
        
    def update(self): #рандомное расположение 
        #self.rect.center = (random.randint(24,WIDTH - 24), random.randint(24,HEIGHT - 24))
        self.rect.center = (random.randint(24,WIDTH - 24), 0)
        self.image = choice(money)
        
    def move(self): # движение по дороге 
        self.rect.move_ip(0, 7)
        if self.rect.bottom > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(24,WIDTH - 24), 0)
    
    def draw(self, surface): # отрисовка
        surface.blit(self.image, self.rect)
    
    def getscore(self): #каждая монетка будет давать свой счет 
        global score_coins
        if self.image == coin1:
            score_coins += 1
        if self.image == coin2:
            score_coins += 3
        if self.image == coin3:
            score_coins += 5
        if self.image == coin4:
            score_coins += 10
        return score_coins

pl = Player() # объект игрока 
en1 = Enemy() # объект противника
c = Coins(choice(money)) # объект монеток

enemies = pygame.sprite.Group() # группа противников 
enemies.add(en1) # добавляем объект в группу 

coins = pygame.sprite.Group() # группа монеток 
coins.add(c) # добавляем объект в группу 

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # закрытие окна 
            finished = True

    pl.update()
    en1.update()

    for enemy in enemies: 
        if score % 10 == 0 and score != 0: # увеличиваем скорость противника когда счет пройденных машинок делится на 10
            enemy.enemy_step = 13
        else:
            enemy.enemy_step = 10

    if pygame.sprite.spritecollideany(pl, enemies): # проверка удара с противником 
        sound1.play()
        sleep(0.5)         
        screen.fill(RED)
        screen.blit(game_over, (30,250)) # вывести надпись проигрыша
        pygame.display.update() 
        sleep(2)
        finished = True # закончить игру 
        
    if pygame.sprite.spritecollideany(pl, coins): # проверка удара с монетками 
        sound.play() 
        #score_coins += 1 
        score_coins = c.getscore() # прибавляем монетки к счету 
        coins.update() 

    screen.blit(background,(0,bgY)) 
    screen.blit(background,(0,bgY2))
    
    # движение заднего фона 
    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED
    
    pl.draw(screen)
    en1.draw(screen)
    c.draw(screen)
    c.move()

    score_img = font.render(f'{score}', True, BLACK)
    screen.blit(score_img, (10, 10))

    score_coins_img = font.render(f'{score_coins}', True, RED)
    screen.blit(score_coins_img, (10, 35))
    
    pygame.display.update()
    clock.tick(FPS)
