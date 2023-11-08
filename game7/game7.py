import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from game_parameters import *
from player import Player
from enemy import Enemy, enemies

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
add_fish(5)
add_enemies(5)

#draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font to keep store
score = 0
score_font = pygame.font.Font("../assets/fonts/Minangrasa.otf", 50)

#add sounds to game
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")

#placeholder for Orange player

#load sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

#add alternate and game over
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0,0,0))

#set lives
lives = NUM_LIVES

while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        #player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("You pressed the key up key")
                player.move_up()
            if event.key == pygame.K_s:
                print("You pressed the down key")
                player.move_down()
            if event.key == pygame.K_a:
                print("You pressed the left key")
                player.move_left()
            if event.key == pygame.K_d:
                print("You pressed the right key")
                player.move_right()

        if event.type == pygame.KEYUP:
            player.stop()

    #blit background
    screen.blit(background,(0,0))

    #update fish position
    fishes.update()

    #update player fish
    player.update()

    enemies.update()

    #check for collisions between player and fish/enemy
    result = pygame.sprite.spritecollide(player, fishes, True)
    result2 = pygame.sprite.spritecollide(player, enemies, True)

    #print(result)
    if result:
        #play sounds
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        add_fish(len(result))

    if result2:
        #play sounds
        pygame.mixer.Sound.play(hurt)
        lives -= len(result2)
        score -= len(result2)
        add_enemies(len(result2))

    #check if fish left the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            x = random.randint(screen_width, screen_width*2)
            y = random.randint(0, screen_height-(tile_size*2))
            fishes.add(Fish(x,y))

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            x = random.randint(screen_width, screen_width*2)
            y = random.randint(0, screen_height-(tile_size*2))
            enemies.add(Enemy(x,y))

    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    # update score on screen
    text = score_font.render(f"{score}", True, (50, 81, 123))
    screen.blit(text, (screen_width - text.get_width() / 2 - 40, screen_height / 10 - text.get_height() / 2))

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height-tile_size))

    pygame.display.flip()

    clock.tick(60)

#create new background whengame over
screen.blit(background, (0,0))

#show game over message
message = score_font.render("GAME OVER", True, (0,0,0))
screen.blit(message, (screen_width / 2- message.get_width() / 2, screen_height / 2))

#show final score
score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height / 2 +score_text.get_height()))
#update display
pygame.display.flip()

#play game over sound effect
pygame.mixer.Sound.play(bubbles)

#wait for user to exit game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
