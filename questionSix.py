import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((800,600))
gluPerspective(45, (800/600), 0.1, 50.0)
glTranslatef(0,0,-5)

def draw_lines(x1, y1, x2, y2):
    glBegin(GL_LINES)  # Start drawing a triangle
    glColor3f(1, 0, 0)     # red
    glVertex2f(x1, y1) # Bottom left
    glColor3f(0, 1, 0)     # green
    glVertex2f(x1, y1) # Bottom left
    glEnd()

while True:
    for abc in pygame.event.get():
        # screen.fill((0, 0, 0))
        if abc.type == pygame.QUIT:
            pygame.quit()
        elif abc.type == KEYDOWN:
            if abc.key == K_ESCAPE:
                pygame.quit()
    pygame.display.flip()