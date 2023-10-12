import pygame
import sys

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#colors:
MET_BLUE = (50,82,123)
LIGHT_BROWN = (205,173,132)

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue background with brown sandy bottom")

#Main loop
running = True #set flag to true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with blue
    screen.fill(MET_BLUE)
    #add sandy bottom
    rectangle_height = 100
    pygame.draw.rect(screen, LIGHT_BROWN, (0, screen_height-rectangle_height, screen_width, rectangle_height))

    #update the display
    pygame.display.flip()