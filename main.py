import pygame
import random
from road import Road
from  world import roads1
from  world import roads2
from car import Car
from world import matrix
from world import World
pygame.init()

matrix = matrix


screen = pygame.display.set_mode((800, 800))

running = True
clock = pygame.time.Clock()
a = Car(roads2[0]*25, 0, 1, 0, 1)

My_world = World(matrix, screen)
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    My_world.draw()
    a.draw(screen)


    pygame.display.flip()

    clock.tick(60)
