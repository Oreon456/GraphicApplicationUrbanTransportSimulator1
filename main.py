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
a = Car(roads2[0]*25, 0, 5, 0, 1)




def generate_cars(cnt):
    cars = []
    for i in range(cnt):

        cars.append(Car(random.choice(roads2)*25, 0, 5, 0, 1))
    return cars

cnt =100
My_world = World(matrix, screen)
objects = []
while running:
    objects = objects+generate_cars(cnt)
    cnt = 0
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    My_world.draw()
    for i in objects:
        if not i.draw(screen):
            objects.remove(i)
            cnt+=1



    pygame.display.flip()

    clock.tick(60)