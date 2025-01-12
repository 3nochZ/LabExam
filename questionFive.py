import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
pygame.display.set_mode((800,600))
gluPerspective(45, (800/600), 0.1, 50.0)
glTranslatef(0,0,-5)

glBegin(GL_TRIANGLES)  # Start drawing a triangle
glColor3f(1, 0, 0)     # Set color to red
glVertex2f(-0.5, -0.5) # Bottom left
glColor3f(0, 1, 0)     # Set color to green
glVertex2f(0.5, -0.5)  # Bottom right
glColor3f(0, 0, 1)     # Set color to blue
glVertex2f(0.0, 0.5)   # Top
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