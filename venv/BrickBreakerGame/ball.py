import pygame
from random import randint

BLACK = (0, 0, 0)
MAX_VELOCITY = 13 #Max speed of ball
VELOCITY_PER = 0.25 #Change per bounce

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), 4]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = randint(-8, 8)
        if abs(self.velocity[1]) < MAX_VELOCITY:
            if self.velocity[1] < 0:
                self.velocity[1] = -self.velocity[1]  + VELOCITY_PER
            else:
                self.velocity[1] = -self.velocity[1]  - VELOCITY_PER
        else:
            self.velocity[1] = -self.velocity[1]
