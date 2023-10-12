import pygame
import sys
import random

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("using blit to draw tiles")

def draw_background(screen):
    #load our tiles from assets folder
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #make pngs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    #fill screen with sand
    for x in range(0, screen_width, tile_size):
        for y in range(screen_height-tile_size, screen_height, tile_size):
            screen.blit(sand, (x,y))

    # fill screen with sand
    for _ in range(4):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x,screen_height- 2 * tile_size))


#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    pygame.display.flip()

pygame.quit()

