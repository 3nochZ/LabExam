import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Four")

    while True:
        for abc in pygame.event.get():
            if abc.type == pygame.QUIT:  # default quit
                pygame.quit()
            elif abc.type == KEYDOWN:
                if abc.key == K_F1:  # alternative quit using the key F1
                    pygame.quit()
        screen.fill((255, 255, 255))

        # B

        # pygame.draw.line(screen, RED, (50, 50), (250, 250), 3)

        #C
        pygame.draw.polygon(screen, BLUE, ((250, 0),(150, 150),(0,0)))

        #D - Point
        pygame.draw.line(screen, GREEN, (250, 250), (251, 251), 1)
        pygame.display.update()


main()  # Test