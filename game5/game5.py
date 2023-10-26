import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

#Initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Adding a player fish")

#clock object
clock = pygame.time.Clock()

#Main Loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2),random.randint(0, screen_height-(tile_size*2))))

#draw player fish
player = Player(screen_width/2, screen_height/2)

#placeholder for Orange player

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
                player.move_up()
            if event.key == pygame.K_DOWN:
                print("You pressed the down key")
                player.move_down()
            if event.key == pygame.K_LEFT:
                print("You pressed the left key")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print("You pressed the right key")
                player.move_right()

    #blit background
    screen.blit(background,(0,0))

    #update fish position
    fishes.update()

    #update player fish
    player.update()

    #check if fish left the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            x = random.randint(screen_width, screen_width*2)
            y = random.randint(0, screen_height-(tile_size*2))
            fishes.add(Fish(x,y))

    fishes.draw(screen)

    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()