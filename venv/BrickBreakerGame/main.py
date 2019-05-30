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

#Rows
BLUE_ROW = 150
GREEN_ROW = 100
YELLOW_ROW = 50

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

moving_sprites = pygame.sprite.Group()
moving_sprites.add(playerPaddle)
moving_sprites.add(ball)

blue_brick1 = Brick(BLUE, 50, 15)
blue_brick1.rect.x = 75
blue_brick1.rect.y = BLUE_ROW

blue_brick2 = Brick(BLUE, 50, 15)
blue_brick2.rect.x = 175
blue_brick2.rect.y = BLUE_ROW

blue_brick3 = Brick(BLUE, 50, 15)
blue_brick3.rect.x = 275
blue_brick3.rect.y = BLUE_ROW

blue_brick4 = Brick(BLUE, 50, 15)
blue_brick4.rect.x = 375
blue_brick4.rect.y = BLUE_ROW

blue_brick5 = Brick(BLUE, 50, 15)
blue_brick5.rect.x = 475
blue_brick5.rect.y = BLUE_ROW

blue_brick6 = Brick(BLUE, 50, 15)
blue_brick6.rect.x = 575
blue_brick6.rect.y = BLUE_ROW

green_brick1 = Brick(GREEN, 50, 15)
green_brick1.rect.x = 125
green_brick1.rect.y = GREEN_ROW

green_brick2 = Brick(GREEN, 50, 15)
green_brick2.rect.x = 225
green_brick2.rect.y = GREEN_ROW

green_brick3 = Brick(GREEN, 50, 15)
green_brick3.rect.x = 325
green_brick3.rect.y = GREEN_ROW

green_brick4 = Brick(GREEN, 50, 15)
green_brick4.rect.x = 425
green_brick4.rect.y = GREEN_ROW

green_brick5 = Brick(GREEN, 50, 15)
green_brick5.rect.x = 525
green_brick5.rect.y = GREEN_ROW

yellow_brick1 = Brick(YELLOW, 50, 15)
yellow_brick1.rect.x = 175
yellow_brick1.rect.y = YELLOW_ROW

yellow_brick2 = Brick(YELLOW, 50, 15)
yellow_brick2.rect.x = 275
yellow_brick2.rect.y = YELLOW_ROW

yellow_brick3 = Brick(YELLOW, 50, 15)
yellow_brick3.rect.x = 375
yellow_brick3.rect.y = YELLOW_ROW

yellow_brick4 = Brick(YELLOW, 50, 15)
yellow_brick4.rect.x = 475
yellow_brick4.rect.y = YELLOW_ROW

static_sprites = pygame.sprite.Group()
static_sprites.add(blue_brick1)
static_sprites.add(blue_brick2)
static_sprites.add(blue_brick3)
static_sprites.add(blue_brick4)
static_sprites.add(blue_brick5)
static_sprites.add(blue_brick6)
static_sprites.add(green_brick1)
static_sprites.add(green_brick2)
static_sprites.add(green_brick3)
static_sprites.add(green_brick4)
static_sprites.add(green_brick5)
static_sprites.add(yellow_brick1)
static_sprites.add(yellow_brick2)
static_sprites.add(yellow_brick3)
static_sprites.add(yellow_brick4)


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
            static_sprites.remove(brick) # delete brick from sprite list
            brick.remove() # delete brick itself
            if brick.rect.y == BLUE_ROW:
                score += 1
            if brick.rect.y == GREEN_ROW:
                score += 3
            if brick.rect.y == YELLOW_ROW:
                score += 5

    moving_sprites.update()
    screen.fill(BLACK) #Background
    pygame.draw.line(screen, WHITE, [0,500], [700, 500], 5) #Bottom, hit = death
    moving_sprites.draw(screen) #Add sprites to screen
    static_sprites.draw(screen)

    font = pygame.font.Font(None, 50)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    font = pygame.font.Font(None, 50)
    text = font.render("Speed: " + str(ball.velocity[1]), 1, WHITE)
    screen.blit(text, (490, 10))

    pygame.display.flip() #Update screen
    clock.tick(60) #fps

pygame.quit()