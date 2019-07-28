import math
import pygame
import numpy as np
import numpy.linalg as la
from util import *

class Image():
    def __init__(self, rays):
        self.rays = rays

    def draw1D(self, position, window):
        pixels = [ray.color for ray in self.rays]
        for pixel in reversed(pixels):
            pygame.draw.rect(window, pixel, (position.x, position.y, 5, 30))
            position.x += 5

    def draw2D(self, position, window):
        pixels = [ray.color for ray in self.rays]
        heights = [ray.distance for ray in self.rays]
        #heights = [abs(ray.distance * math.cos(angle_between([0,1],ray.direction.toNumpy()))) for ray in self.rays]

        pygame.draw.rect(window, (65, 65, 56), (position.x, position.y, MAP_WIDTH, 200))

        for pixel,height in zip(reversed(pixels),reversed(heights)):
            offset =  min(200,height/2) /2
            shading = offset/100
            print("shading",shading)
            pygame.draw.rect(window, BLACK, (position.x, position.y, 5, offset))
            color = shade_color(pixel,shading)
            print(color)
            pygame.draw.rect(window, color, (position.x,  position.y + offset, 5, 200-(2*offset)))
            position.x += 5

