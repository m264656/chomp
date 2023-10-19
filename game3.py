import pygame
import sys
import random
from fish import Fish, fishes #importing sprite class and sprite Group

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("using blit to draw tiles")

#load game font
custom_font = pygame.font.Font("assets/fonts/RushdaFunky.otf", 100)

def draw_background(screen):
    #load our tiles from assets folder
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #make pngs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    # fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

    # fill screen with sand
    for x in range(0, screen_width, tile_size):
        for y in range(screen_height - tile_size, screen_height, tile_size):
            screen.blit(sand, (x, y))

    # fill screen with grass
    for _ in range(5):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height - 2 * tile_size))

    # draw the text
    text = custom_font.render("Chomp", True, (50,81,123))
    screen.blit(text,(screen_width/2-text.get_width()/2, screen_height/10-text.get_height()/2))


# main loop
running = True
background = screen.copy()
draw_background(background)

# draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(0, screen_width-tile_size),random.randint(0, screen_height-(tile_size*2))))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    #draw fish objects
    fishes.draw(background)

    pygame.display.flip()
