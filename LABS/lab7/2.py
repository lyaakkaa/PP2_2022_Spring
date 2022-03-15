import pygame
pygame.init()
import os

#Global Variables
WIDTH = 600
HEIGHT = 600

FPS = 20

vol = 1.0


#Initialiazing
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("TEST PROGRAM")
clock =  pygame.time.Clock()
finished = False

pygame.mixer.music.load("./music/Glass Animals - Heat waves.mp3")
pygame.mixer.music.play(-1)
song_list = os.listdir('./music')
print(song_list)
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            vol -= 0.1
            pygame.mixer.music.set_volume(vol)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            vol += 0.1
            pygame.mixer.music.set_volume(vol)


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.mixer.music.unpause()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for song in range(1,len(song_list)):
                pygame.mixer.music.load(f'./music/{song_list[song]}')
                pygame.mixer.music.play(-1)

        

    pygame.display.flip() #IMPORTANT TO WRITE
pygame.quit()