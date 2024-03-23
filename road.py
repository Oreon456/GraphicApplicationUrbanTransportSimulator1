import pygame

class Road:
    def __init__(self, direction, car=False):
        self.direction = direction #up/down or left/right or intersection
        self.car = car
    def car_is_on_the_tile(self):
        self.car = True
    def car_off_tile(self):
        self.car = False
    def is_car(self):
        return self.car