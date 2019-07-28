import math
import pygame
import numpy as np
from util import *
from geometrics import Point, Circle


class Ray():
    def __init__(self, origin, angle):
        self.origin = origin
        self.initial_angle = angle
        self.angle = angle
        self.direction = Position(
            math.sin(self.initial_angle),
            math.cos(self.initial_angle))
        #self.direction = Position(1,1)
        self.target = self.origin
        self.maxlength = 4000
        self.color = BLACK
        self.distance = self.maxlength

    def show(self, window):
       pygame.draw.line(window, WHITE, self.origin.toTuple(), self.target.toTuple(), 2)

    def change_dir(self, angle):
        self.angle = angle
        self.direction = Position(
            math.sin(angle),
            math.cos(angle))

    def update_target(self, point):
        self.target = point.center

    def line_intersect(self, target):
        x1 = target.a.x
        y1 = target.a.y
        x2 = target.b.x
        y2 = target.b.y
        x3 = self.origin.x
        y3 = self.origin.y
        x4 = self.origin.x+self.direction.x
        y4 = self.origin.y+self.direction.y
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = (-1 * ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))) / den
        #print("-"*12)
        #print(t)
        #print(u)

        if (t >= 0 and t < 1 and u > 0):
            ptx = x1 + (t * (x2 - x1))
            pty = y1 + (t * (y2 - y1))
            point = Point(int(ptx), int(pty))
            return point
        else:
            return None

