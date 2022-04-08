import pygame
from random import randrange
pygame.init() # инициализируем pygame

WIDTH, HEIGHT = 400, 450 # высота и ширина окна

cell = 20 #размер клетки 

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (175, 238, 238)
PINK = (255,192,203)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #экран
pygame.display.set_caption('SNAKE') # название окна 

background = pygame.image.load('./snake_img/sand.jpg') # загружаем картинку заднего фона
background = pygame.transform.scale(background,(WIDTH, HEIGHT- 50)) # трансформируем по размерам окна - 50 потому что нижняя часть без фона
apple = pygame.image.load('./snake_img/apple.png') # загружаем картинку яблока 
apple_Score = pygame.image.load('snake_img/apple_score.png') # загружаем картинку яблока 
level_up = pygame.image.load('snake_img/level-up.png') # загружаем картикну левел апа
br = pygame.image.load('./snake_img/brick-wall.png') # загружаем картинку кирпичика

font = pygame.font.SysFont("Verdana", 20) # шрифт  
font1 = pygame.font.SysFont("Verdana", 14) # шрифт
clock = pygame.time.Clock() # время

sound = pygame.mixer.Sound('./snake_sounds/biting.wav') # звук откусывания яблока 


class Food:  # класс Еды 
    def __init__(self):
        self.x = randrange(0, WIDTH, cell) # координаты яблкока по х 
        self.y = randrange(0, HEIGHT - 50, cell) # координаты яблкока по у 

    def draw(self):  # функция отрисовки 
        fruit_rect = pygame.Rect(self.x, self.y, cell, cell)  # ректангл для яблока 
        screen.blit(apple, fruit_rect) # размещаем картинку яблока на ректангл 

        #pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell)) 

    def redraw(self): # функция отрисовки заново 
        self.x = randrange(0, WIDTH, cell)   # координаты яблкока по х 
        self.y = randrange(0, HEIGHT - 50, cell) # координаты яблкока по у 
'''
класс Стенок без картинок 
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))'''

class Wall: # Класс стенок 
    def __init__(self, x, y):
        self.x = x # координаты стенки по х
        self.y = y # координаты стенки по у 

        # создаем пространство для картинки кирпичиков
        self.surf = pygame.Surface((cell, cell))
        self.rect = self.surf.get_rect(topleft = (self.x, self.y)) 

    def draw(self):  # функция отрисовки
        self.surf.blit(br ,(0 , 0))
        screen.blit(self.surf, self.rect)

class Snake: # Класс змейки
    def __init__(self):
        self.speed = cell # скорсоть змейки
        self.body = [[80, 80]] # массив змейки 
        self.dx = self.speed  #скорость по х
        self.dy = 0 # скорость по у 
        self.destination = '' # направление змейки 

    
    def move(self):
        for event in events: # проверяем все действия 
            if event.type == pygame.KEYDOWN: # если нажимаем на клавишу 
                if event.key == pygame.K_LEFT and self.destination != 'right': # если нажимаем на левую клавишу и змейка не направлена на право
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left': # если нажимаем на правую клавишу и змейка не направлена на лево
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down': # если нажимаем на верхнюю клавишу и змейка не направлена вниз
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up': # если нажимаем на нижнюю клавишу и змейка не направлена на вверх
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'

        for i in range(len(self.body) - 1, 0, -1): # добавление блока в тело змейки 
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        
        self.body[0][0] += self.dx  # двигаем постоянно
        self.body[0][1] += self.dy  # двигаем постоянно

        self.body[0][0] %= WIDTH  # проверяем чтоб голова по х не прошла за окно
        self.body[0][1] %= HEIGHT - 50 # проверяем чтоб голова по у не прошла за окно

    def draw(self): # функция отрисовки 
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell),4) 
    
    def collide_food(self, f:Food): #функция проверки столкновения с едой 
        global score
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            sound.play()
            self.body.append([1000, 1000])
            score += 1
            
    def collide_self(self):
        global finished, lose
        if self.body[0] in self.body[1:]:
            finished = True
            lose = True

    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()

restart = True

while restart:

    level = 0
    score = 0 
    finished = False
    lose = False
    win = False
    s = Snake()
    f = Food()
    FPS = 5

    while not finished:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
                restart = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                level += 1
        
        screen.fill(PINK)    
        screen.blit(background, (0, 0))
        
        screen.blit(apple_Score, (25,410))
        screen.blit(level_up,(345,410))

        text_game_over = font1.render(f'  Game Over! your score {score}', True, RED)
        text_win = font1.render(f'             You won!', True, RED)
        restart_text = font1.render(f'Tap space to restart', True, RED)

        f.draw()
        s.draw()
        s.move()
        s.collide_food(f)
        s.collide_self()
        s.check_food(f)
       
        if score == 5:
            score = 0
            level += 1
            FPS += 5
        if level == 4:
            win = True

        walls_coor = open(f'wall{level}.txt', 'r').readlines()
        walls = []
        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Wall(j * cell, i * cell))
        for wall in walls:
            wall.draw()
            if f.x == wall.x and f.y == wall.y:
                f.redraw()
            if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
                #finished = True
                lose = True

        while lose or win:
            pygame.draw.rect(screen, WHITE, (100, 100, 200, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    lose = False
                    win = False
                    finished = True
            if lose:
                screen.blit(text_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
                screen.blit(restart_text, (WIDTH // 2 - 74, HEIGHT // 2 - 30))
            if win:
                screen.blit(text_win, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
                screen.blit(restart_text, (WIDTH // 2 - 74, HEIGHT // 2 - 30))
    
            pygame.display.flip()
        

        render_score = font.render(f'{score}', True, RED)
        render_level_up = font.render(f'{level}', True, YELLOW)

        screen.blit(render_score,(55, 410))
        screen.blit(render_level_up,(325, 410))

        pygame.display.flip()
    pygame.display.flip()
pygame.quit()