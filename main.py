import pygame
import sys
from settings import *
from debug import debug
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        
        # , pygame.FULLSCREEN     paste this in later for full screen after HEIGHT)  
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN ) # setmode sets the display screen and how big it is, works with display surface

        
        # names the game in the header
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        
        self.level = Level()

    def run(self): # self as a arg makes it use all the other things within the class, it's good practice
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()  # Allow quitting with ESC key

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
