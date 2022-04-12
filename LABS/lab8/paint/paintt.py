import pygame
pygame.init() # инициализируем pygame


WIDTH, HEIGHT = 800, 800 # размеры окна 
FPS  = 60

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # экран
pygame.display.set_caption("Paint_lyaka") # название окна

clock = pygame.time.Clock()

screen.fill(WHITE) # заполнение белым цветом 
colors = pygame.image.load('./images/colors.png') 
colors = pygame.transform.scale(colors, (100, 100))

running = True
RAD = 30
drawing = False 
color = BLACK

start_pos = 0
end_pos = 0

pen_mode = 0 # режим рисования 

def rectan(color, pos, width, height): # функция прорисовки прямоугольников
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def circle(color, pos, rad): # функция прорисовки окружностей
    pygame.draw.circle(screen, color, pos, rad, 4)

def eraser(pos,rad): # ластик 
    pygame.draw.circle(screen, WHITE, pos, rad)

while running:
    clock.tick(FPS)

    pos = pygame.mouse.get_pos()
    screen.blit(colors, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # проверка на закрытие окна 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # если мы нажали на мышку 
            drawing = True
            start_pos = pos
            if pos[0] > 0 and pos[0] < 100 and pos[1] > 0 and pos[1] < 100:
                color = screen.get_at(pos) # берем нужный цвет
        
        if event.type == pygame.MOUSEBUTTONUP: #  если отпустили мышку то отрисовка
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1]) 

            # проверка режимов 
            if pen_mode == 0:
                
                rectan(color, start_pos, rect_x, rect_y)
            elif pen_mode == 1:
                circle(color, start_pos, rect_x)
        # ластик     
        if event.type == pygame.MOUSEMOTION and drawing:
            if pen_mode == 2:
                eraser(pos, RAD)
        # смена режимов 0 - ректангл, 1 -круг, 2 - ластик
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pen_mode = 0
            if event.key == pygame.K_1:
                pen_mode = 1
            if event.key == pygame.K_2:
               pen_mode = 2
            if event.key == pygame.K_BACKSPACE:
                screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()       
