from time import sleep
import pygame
import random
pygame.init()


FPS = 60 
WIDTH, HEIGHT = 400, 600
step = 5
enemy_step = 10

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

score = 0 #time 
score_coins = 0 #SCORE

#fonts
font = pygame.font.SysFont("Verdana", 20)
font1 = pygame.font.SysFont("Verdana", 60)
game_over = font1.render("Game Over", True, BLACK)

#display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars")

#load pictures
background = pygame.image.load('./images/bkg.png')

#переменные для движения заднего фона
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 5
#load sounds 
sound = pygame.mixer.Sound("./music_cars/dollar.wav")
sound1 = pygame.mixer.Sound("./music_cars/crush.mp3")

class Player(pygame.sprite.Sprite): # класс игрока 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def update(self):  #движение 
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

class Enemy(pygame.sprite.Sprite):  # класс противников 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40 ),0)
    
    def update(self): #движение 
        global score
        self.rect.move_ip(0, enemy_step)
        if self.rect.bottom > HEIGHT:
            score += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
   
    def draw(self, surface): # Отрисовка
        surface.blit(self.image, self.rect)

class Coins(pygame.sprite.Sprite): # класс монеток 

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/dollar.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24,WIDTH - 24), random.randint(24 ,HEIGHT - 24))
       
    def update(self): # рандомное появление монеток 
        #self.rect.center = (random.randint(24,WIDTH - 24), random.randint(24,HEIGHT - 24))
        self.rect.center = (random.randint(24,WIDTH - 24), 0)
        
    def move(self): # движение вниз
        self.rect.move_ip(0, 7)
        if self.rect.bottom > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(24,WIDTH - 24), 0)

    def draw(self, surface): # отрисовка 
        surface.blit(self.image, self.rect)
    

pl = Player() # объект игрока 
en1 = Enemy() # объект противника 
c = Coins() #объект монетки 

enemies = pygame.sprite.Group() # группа противников 
enemies.add(en1) # добавление противника в группу 

coins = pygame.sprite.Group() # группа монеток
coins.add(c) # добавление монетки в группу 

finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #проверка на закрытие окна 
            finished = True

    pl.update()
    en1.update()

    if pygame.sprite.spritecollideany(pl, enemies): # проверка столкновения игрока с противников 
        sound1.play()
        sleep(0.5)         
        screen.fill(RED)
        screen.blit(game_over, (30,250))
        pygame.display.update() 
        sleep(2)
        finished = True
        
    if pygame.sprite.spritecollideany(pl, coins):  # проверка столкновения игрока с монеткой 
        sound.play()
        score_coins += 1
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
    
    # отоброжение счета 
    score_img = font.render(f'{score}', True, BLACK)
    screen.blit(score_img, (10, 10))

    score_coins_img = font.render(f'{score_coins}', True, RED)
    screen.blit(score_coins_img, (10, 35))
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

    






