import pygame
import random
import numpy as np
from util import *

WHITE = (255,255,255)

class Boundary():
    def __init__(self, x1, y1, x2, y2):
        self.a = Position(x1,y1)
        self.b = Position(x2,y2)
        self.color = (random.randint(80,220), random.randint(80,220), random.randint(80,220))

    def show(self, window):
        pygame.draw.line(window, self.color, self.a.toTuple(), self.b.toTuple(), 5)


class Frame():
    def __init__(self, x, y, width, height):
        self.left_boundary = Boundary(x,y,x,y+height)
        self.right_boundary = Boundary(x+width,y,x+width,y+height)
        self.top_boundary = Boundary(x, y, x+width, y)
        self.bottom_boundary = Boundary(x, y+height, x+width, y+height)
        self.set_color(BLACK)

    def get_boundaries(self):
        yield self.left_boundary
        yield self.right_boundary
        yield self.top_boundary
        yield self.bottom_boundary

    def set_color(self,color):
        for border in self.get_boundaries():
            border.color = color