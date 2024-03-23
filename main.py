import pygame
import random
from road import Road
from car import Car


pygame.init()

screen = pygame.display.set_mode((800, 800))
matrix = [
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [3, 3, 3, 1, 1, 3, 3, 3],
    [3, 3, 3, 1, 1, 3, 3, 3],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0]
]


directs = {1: 'intersection', 2:'up/down', 3: 'left/right'}
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]!=0:
            matrix[i][j] = Road(directs[matrix[i][j]])
running = True
clock = pygame.time.Clock()
a = Car(400, 0, 1, 0, 1)
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    a.draw(screen)

    pygame.display.flip()

    clock.tick(60)
