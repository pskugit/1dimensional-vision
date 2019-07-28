import pygame
import numpy as np
from util import *

WHITE = (255,255,255)
RED = (180,0,0)

class Point():
    def __init__(self, x, y):
        self.center = Position(x,y)
        self.radius = 5

    def show(self, window):
        pygame.draw.circle(window, RED, self.center.toTuple(), self.radius, 1)

    def toTuple(self):
        return self.center.toTuple()

class Circle():
    def __init__(self, x, y, radius):
        self.center = Position(x,y)
        self.radius = radius

    def show(self, window):
        pygame.draw.circle(window, WHITE, self.center.toTuple(), self.radius, 1)
