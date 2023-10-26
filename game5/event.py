import pygame
import sys

from game_parameters import *
from background import draw_background #import draw background function

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("learning to get event types")

#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
            if event.key == pygame.K_DOWN:
                print("You pressed the down key")
            if event.key == pygame.K_LEFT:
                print("You pressed the left key")
            if event.key == pygame.K_RIGHT:
                print("You pressed the right key")


    #draw the background
    screen.blit(background, (0,0))

    #flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()


