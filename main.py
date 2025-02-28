import pygame
from player import Player #for some reason, import player isn't enough
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for ast in asteroids: 
            if ast.collides_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if ast.collides_with(shot):
                    shot.kill()
                    ast.kill()

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000 #limit framerate
        

if __name__ == "__main__":
    main()