import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 45

background = pygame.transform.scale(pygame.image.load(r".\images\bg.jpeg"), (WIDTH, HEIGHT))
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 7


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cars')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 500
        self.speed = 10
        self.image = pygame.transform.scale(pygame.image.load('.\images\Audi.png'),(40,90))
        self.surf = pygame.Surface((40,90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center=(self.x,self.y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0,-self.speed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= HEIGHT:
            self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(10, 15)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\images\Police.png"), (40,90))
        self.surf = pygame.Surface((40,90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)

    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(10, 15)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\images\Gold_1.png"), (25,25))
        self.surf = pygame.Surface((25,25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 25)
font_large = pygame.font.SysFont("Times New Roman", 75)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

enemies = pygame.sprite.Group([Enemy() for _ in range(5)])
coins = pygame.sprite.Group([Coin() for _ in range(7)])
p = Player()

SCORE = 0
game_over = font_large.render("GAME OVER", False, BLACK)
finished = False
lose = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.blit(background,(0,bgY))
    screen.blit(background,(0,bgY2))

    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED

    text = font.render(f"SCORE: {SCORE}", False, RED)
    screen.blit(text, (50,20))

    p.draw()
    p.move()
    
    if len(enemies) < 5:
        enemies.add(Enemy())
    if len(coins) < 7:
        coins.add(Coin())

    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.kil()

    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()

    if pygame.sprite.spritecollide(p, enemies, False):
        lose = True

    for coin in coins:
        if pygame.sprite.collide_rect(p, coin):
            coin.kill()
            SCORE += 1
            coins.add(Coin())

    for enemy in enemies:
        for enemy2 in enemies:
            if enemy != enemy2 and pygame.sprite.collide_rect(enemy, enemy2):
                enemy2.kill()
    
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False
        pygame.draw.rect(screen, WHITE, (100, 75, 600, 400))
        screen.blit(game_over, (100,100))
        pygame.display.flip()

    pygame.display.flip()
pygame.quit()