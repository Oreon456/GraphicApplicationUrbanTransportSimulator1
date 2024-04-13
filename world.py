import pygame
from road import Road
import random





odds = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
even = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
a, b = random.randint(5, 10), random.randint(5, 10)
roads1 = list(set(random.choice(odds) for i in range(a)))
roads2 = list(set(random.choice(even) for j in range(b)))



matrix = [[0]*32]
for i in range(31):
    matrix.append([0]*32)

for x in roads1:
    for i in range(32):
        matrix[x][i] = 3

for x in roads2:
    for i in range(32):
        if matrix[i][x]!=0:
            matrix[i][x]=1
        else:
            matrix[i][x]=2




for i in range(len(matrix)):
    print(*matrix[i])





directs = {1: 'intersection', 2:'up/down', 3: 'left/right'}
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]!=0:
            matrix[i][j] = Road(directs[matrix[i][j]])


class World:
    def __init__(self, map, screen):
        self.map=map
        self.screen = screen
    def draw(self):
        for j in range(len(self.map)):
            for i in range(len(self.map)):
                if type(self.map[j][i])!=int:
                    pygame.draw.rect(self.screen, 'black', pygame.Rect(i*25, j*25, i*25+25, j*25+25))
                else:
                    pygame.draw.rect(self.screen, 'green', pygame.Rect(i * 25, j *25, i * 25 + 25, j * 25 + 25))



