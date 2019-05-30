import pygame
from paddle import Paddle
from ball import Ball
from Brick import Brick
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
score = 0

playerPaddle = Paddle(WHITE, 100, 10)
playerPaddle.rect.x = 300
playerPaddle.rect.y = 470

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

brick1 = Brick(BLUE, 50, 15)
brick1.rect.x = 100
brick1.rect.y = 150

brick2 = Brick(BLUE, 50, 15)
brick2.rect.x = 200
brick2.rect.y = 150

brick3 = Brick(BLUE, 50, 15)
brick3.rect.x = 300
brick3.rect.y = 150

brick4 = Brick(BLUE, 50, 15)
brick4.rect.x = 400
brick4.rect.y = 150

brick5 = Brick(BLUE, 50, 15)
brick5.rect.x = 500
brick5.rect.y = 150

brick6 = Brick(BLUE, 50, 15)
brick6.rect.x = 600
brick6.rect.y = 150

brick7 = Brick(GREEN, 50, 15)
brick7.rect.x = 150
brick7.rect.y = 100

moving_sprites = pygame.sprite.Group()
moving_sprites.add(playerPaddle)
moving_sprites.add(ball)

static_sprites = pygame.sprite.Group()
static_sprites.add(brick1)
static_sprites.add(brick2)
static_sprites.add(brick3)
static_sprites.add(brick4)
static_sprites.add(brick5)
static_sprites.add(brick6)
static_sprites.add(brick7)

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
        carryOn = False
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, playerPaddle):
        ball.bounce()

    for brick in static_sprites:
        if pygame.sprite.collide_mask(ball, brick):
            ball.bounce()
            if brick.rect.y == 150:
                brick.rect.x = 1000
                score += 1
            if brick.rect.y == 100:
                brick.rect.x = 1000
                score += 3

    moving_sprites.update()
    screen.fill(BLACK) #Background
    pygame.draw.line(screen, WHITE, [0,500], [700, 500], 5) #Bottom, hit = death
    moving_sprites.draw(screen) #Add sprites to screen
    static_sprites.draw(screen)

    font = pygame.font.Font(None, 50)
    text = font.render(str(score), 1, WHITE)
    screen.blit(text, (70, 10))

    pygame.display.flip() #Update screen
    clock.tick(60) #fps

pygame.quit()