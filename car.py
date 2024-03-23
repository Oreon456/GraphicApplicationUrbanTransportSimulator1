from road import Road
import pygame
import random





directions_math_transcriptor = {'intesection': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'left/right': [[1, 0], [-1, 0]], 'up/down':[[0, 1], [0, -1]]}

def get_new_direction(prev, l):
    a = random.choice(l)
    while a!=prev:
        a = random.choice(l)
    return a


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

class Car:
    def __init__(self, x, y, speed, dir1, dir2): # dir1 и dir2 могут быть 1 -1 и 0
        self.x, self.y = x, y
        self.speed = speed
        self.dir1 = dir1
        self.dir2 = dir2
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.tile = (self.x//100, self.y//100)
    def update(self):

        p_x, p_y = self.x+self.speed*self.dir1, self.y+self.speed*self.dir2

        tile1 = (p_x//100, p_y//100)
        print(tile1)

        try:

            if (matrix[tile1[0]][tile1[1]])!=0:
                if tile1!=self.tile:
                    print('wassap')
                    self.tile = tile1
                    list_of_choices = directions_math_transcriptor(matrix[self.tile[0][self.tile[1]]])
                    print('list_of_choices')
                    new_dir = get_new_direction([self.dir1, self.dir2], list_of_choices)
                    self.dir1, self.dir2 =new_dir[0], new_dir[1]
                    print('new_cords')
                    print(self.dir1, self.dir1)
                self.x, self.y = p_x, p_y
            return True
        except:
            return False

    def draw(self, screen):

        response = self.update()
        if response:
            screen.blit(self.image, (self.x, self.y))

