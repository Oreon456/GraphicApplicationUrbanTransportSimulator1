import pygame
import random
from world import matrix


matrix = matrix

directions_math_transcriptor = {'intesection': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'left/right': [[1, 0], [-1, 0]], 'up/down':[[0, 1], [0, -1]]}

def get_new_direction(prev, l):
    prev = [prev[0]*-1, prev[1]*-1]
    a = random.choice(l)
    while a==prev:
        a = random.choice(l)
    return a




class Car:
    def __init__(self, x, y, speed, dir1, dir2, type): # dir1 и dir2 могут быть 1 -1 и 0
        self.car_type = type
        self.x, self.y = x, y
        self.speed = speed
        if self.car_type==1:
            self.speed-=1

        self.dir1 = dir1
        self.dir2 = dir2

        if self.car_type == 1:
            self.size1 = 25
            self.size2 = 10
        else:
            self.size1 = 10
            self.size2 = 10

        self.image = pygame.Surface((self.size2, self.size1))
        if self.car_type==1:

            self.image.fill((255, 0, 0))
        else:
            self.image.fill((0, 0, 255))
        self.tile = (self.x//25, self.y//25)
        self.tile = self.tile[::-1]
    def update(self):

        directions_math_transcriptor = {'intersection': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'left/right': [[1, 0], [-1, 0]], 'up/down': [[0, 1], [0, -1]]}

        p_x, p_y = self.x+self.speed*self.dir1, self.y+self.speed*self.dir2

        tile1 = (p_x//25, p_y//25)
        tile1 = tile1[::-1]



        try:

            if (matrix[tile1[0]][tile1[1]])!=0:


                if tile1!=self.tile:
                    self.tile = tile1

                    list_of_choices = directions_math_transcriptor[matrix[self.tile[0]][self.tile[1]].direction]
                    print(matrix[self.tile[0]][self.tile[1]].direction)
                    print(matrix[self.tile[0]][self.tile[1]].direction, self.tile)
                    print(matrix[self.tile[0]][self.tile[1]], list_of_choices)
                    print(list_of_choices)

                    new_dir = get_new_direction([self.dir1, self.dir2], list_of_choices)
                    if self.dir1!=new_dir[0]:
                        self.size1, self.size2 = self.size2, self.size1
                        self.image = pygame.Surface((self.size2, self.size1))
                        if self.car_type == 1:

                            self.image.fill((255, 0, 0))
                        else:
                            self.image.fill((0, 0, 255))

                    self.dir1, self.dir2 =new_dir[0], new_dir[1]
                if self.dir1==1:
                    self.x=p_x
                    self.y = self.tile[0]*25+15
                elif self.dir1==-1:
                    self.x = p_x
                    self.y = self.tile[0] * 25
                elif self.dir2==-1:
                    self.y = p_y
                    self.x = self.tile[1] * 25 + 15
                elif self.dir2==1:
                    self.y = p_y
                    self.x = self.tile[1] * 25
            return True
        except:
            print('false')
            return False

    def draw(self, screen):

        response = self.update()
        if response:
            screen.blit(self.image, (self.x, self.y))
        return response