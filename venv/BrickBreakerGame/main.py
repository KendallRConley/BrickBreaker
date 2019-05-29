import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

#Colors to use
BLACK = (0, 0, 0) #For background
WHITE = (255, 255, 255) #For paddle and ball
BLUE = (0, 0, 255) #For first layer, 1 point
GREEN = (0, 255, 0) #For second layer, 3 points
YELLOW = (228, 255, 11) #For third layer, 5 points
RED = (255, 0, 0) #For final layer, 7 points

#Open window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")

carryOn = True
clock = pygame.time.Clock()

playerPaddle = Paddle(WHITE, 100, 10)
playerPaddle.rect.x = 300
playerPaddle.rect.y = 450

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(playerPaddle)
all_sprites_list.add(ball)

#main loop
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  #Pressing the x Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerPaddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerPaddle.moveRight(10)

    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, playerPaddle):
            ball.bounce()

    all_sprites_list.update()

    screen.fill(BLACK) #Background
    pygame.draw.line(screen, WHITE, [0,500], [700, 500], 5) #Bottom, hit = death
    all_sprites_list.draw(screen) #Add sprites to screen
    pygame.display.flip() #Update screen
    clock.tick(60) #fps

pygame.quit()