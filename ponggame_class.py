import pygame

# initallize
pygame.init()
pygame.display.set_caption("pong game version 2")

# set up game window

SIZE =(600, 600)
BG_COLOR = (70, 96, 70)
canvas = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# set up paddle:
class paddle:
    def __init__(self, picture, position):
        self.picture = picture
        self.position = position
    def move(self):






