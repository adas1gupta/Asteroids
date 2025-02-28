import pygame
from player import Player #for some reason, import player isn't enough
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 #limit framerate
        player.update(dt)

if __name__ == "__main__":
    main()