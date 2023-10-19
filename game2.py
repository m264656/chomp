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

def draw_fishes(surf):
    #Load our file tiles onto our surface
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png").convert()
    eel = pygame.image.load("assets/sprites/eel.png").convert()
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    red_fish = pygame.image.load("assets/sprites/red_fish.png").convert()

    puffer_fish.set_colorkey((0,0,0))
    eel.set_colorkey((0, 0, 0))
    green_fish.set_colorkey((0, 0, 0))
    red_fish.set_colorkey((0, 0, 0))

    puffer_fish = pygame.transform.flip(puffer_fish, True, False)
    green_fish = pygame.transform.flip(green_fish, True, False)

    #distribute our fish on the screen randomly
    for _ in range(10):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(0, screen_height-tile_size-tile_size)
        fishes = [puffer_fish, eel, green_fish, red_fish]
        random_fish = random.choice(fishes)
        surf.blit(random_fish,(x,y))

#main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes((background))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    pygame.display.flip()

pygame.quit()