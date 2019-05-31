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

PADDLE_SPEED = 15

#Rows
BLUE_ROW = 150
GREEN_ROW = 100
YELLOW_ROW = 50

#Point values
BLUE_VAL = 1
GREEN_VAL = 3
YELLOW_VAL = 5

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

def instantiateBricks():
    for num in range(0, 6):
        brick = Brick(BLUE, 50, 15)
        brick.rect.x = 75 + (100 * num)
        brick.rect.y = BLUE_ROW
        static_sprites.add(brick)

    for num in range(0, 5):
        brick = Brick(GREEN, 50, 15)
        brick.rect.x = 125 + (100 * num)
        brick.rect.y = GREEN_ROW
        static_sprites.add(brick)

    for num in range(0, 4):
        brick = Brick(YELLOW, 50, 15)
        brick.rect.x = 175 + (100 * num)
        brick.rect.y = YELLOW_ROW
        static_sprites.add(brick)

static_sprites = pygame.sprite.Group()
instantiateBricks()

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
        playerPaddle.moveLeft(PADDLE_SPEED)
    if keys[pygame.K_RIGHT]:
        playerPaddle.moveRight(PADDLE_SPEED)

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
                score += BLUE_VAL
            if brick.rect.y == GREEN_ROW:
                score += GREEN_VAL
            if brick.rect.y == YELLOW_ROW:
                score += YELLOW_VAL

    if len(static_sprites) == 0:
        instantiateBricks()

    moving_sprites.update()
    screen.fill(BLACK) #Background
    pygame.draw.line(screen, WHITE, [0,500], [700, 500], 5) #Bottom, hit = death
    moving_sprites.draw(screen) #Add sprites to screen
    static_sprites.draw(screen)

    font = pygame.font.Font(None, 50)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    font = pygame.font.Font(None, 50)
    text = font.render("X Speed: " + str(ball.velocity[0]), 1, WHITE)
    screen.blit(text, (290, 10))

    font = pygame.font.Font(None, 50)
    text = font.render("Y Speed: " + str(ball.velocity[1]), 1, WHITE)
    screen.blit(text, (490, 10))

    pygame.display.flip() #Update screen
    clock.tick(60) #fps

pygame.quit()