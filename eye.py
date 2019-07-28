import pygame
import numpy as np
from ray import *
from util import *
from image import Image

class Eye():
    def __init__(self, position):
        self.position = position
        self.view_angle = 0
        self.rays = [Ray(self.position,math.radians((r-120)/4)) for r in range(240)]
        self.color = RED

    def get_image(self):
        image = Image(self.rays)
        return image

    def update(self):
        self.update_ray_angles()

    def update_ray_angles(self):
        for ray in self.rays:
            ray.change_dir(ray.initial_angle+self.view_angle)

    def rotate(self, direction):
        self.view_angle += direction

    def see(self, scene):
        for ray in self.rays:
            ray.target = self.position
            ray.color = BLACK
            ray.distance = ray.maxlength
            min_intersect = None
            min_distance = ray.maxlength
            for element in scene:
                intersect_point = ray.line_intersect(element)
                if intersect_point is not None:
                    distance = intersect_point.center.eucDistanceTo(ray.origin)
                    #ultimately specifies the valid collision
                    if distance < min_distance:
                        min_intersect = intersect_point
                        min_distance = distance
                        ray.color = element.color
                    #intersect_point.show(self.window)
            if min_intersect is not None:
                ray.target = min_intersect
                ray.distance = min_distance
            else:
                ray.target =  Position(ray.origin.x+ray.direction.x, ray.origin.y+ray.direction.y)


    def show(self, window):
        pygame.draw.circle(window, self.color, self.position.toTuple(), 10, 0)

        s = pygame.Surface((MAP_WIDTH, MAP_HEIGHT+VIEW_HEIGHT))  # the size of your rect
        s.fill(BLACK)
        s.set_colorkey(BLACK)
        s.set_alpha(100)  # alpha level

        for ray in self.rays:
            ray.show(s)

        window.blit(s, (0, 0))  # (0,0) are the top-left coordinates
