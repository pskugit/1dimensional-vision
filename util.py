import math
import pygame
import numpy as np

MAP_WIDTH=1200
MAP_HEIGHT=600
VIEW_WIDTH=1200
VIEW_HEIGHT=200

RED = (180,0,0)
WHITE = (255,255,255)
BLUE = (20,0,220)
BLACK = (0,0,0)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toTuple(self):
        return (int(self.x),int(self.y))

    def toNumpy(self):
        return np.array([self.x, self.y])


    def translate_to(self, position):
        self.x = position.x
        self.y = position.y

    def multipy(self, value):
        return Position(self.x * value, self.y * value)

    def minus(self, position):
        #self.x -= position.x
        #self.y -= position.y
        return Position(self.x - position.x, self.y - position.y)

    def plus(self, position):
        #self.x += position.x
        #self.y += position.y
        return Position(self.x + position.x, self.y + position.y)

    def wrapEdge(self, win_width, win_height):
        wrappedx = (self.x % win_width) - 1
        wrappedy = (self.y % win_height) - 1
        return Position(wrappedx,wrappedy)

    def eucDistanceTo(self, position):
        return math.sqrt(abs(self.x - position.x)**2 +abs(self.y - position.y)**2)

    def __str__(self):
        return("x: {x:.2f}, y: {y:.2f}".format(x=self.x, y=self.y))

def show_text(text, window, position):
    pygame.font.init()
    sys_font = pygame.font.SysFont('lucidasanstypewriterfett', 12)
    window.blit(sys_font.render(text,  0, WHITE), position.toTuple())

def shade_color(color, shade_factor):
    newR = color[0] * (1 - shade_factor)
    newG = color[1] * (1 - shade_factor)
    newB = color[2] * (1 - shade_factor)
    return (newR,newG,newB)


def closest_point_on_seg(seg_a, seg_b, circ_pos):
    seg_v = seg_b - seg_a
    pt_v = circ_pos - seg_a
    seg_v_unit = seg_v / seg_v.len()
    proj = pt_v.dot(seg_v_unit)
    if proj <= 0:
        return seg_a.copy()
    if proj >= seg_v.len():
        return seg_b.copy()
    proj_v = seg_v_unit * proj
    closest = proj_v + seg_a
    return closest

def segment_circle(seg_a, seg_b, circ_pos, circ_rad):
    closest = closest_point_on_seg(seg_a, seg_b, circ_pos)
    dist_v = circ_pos - closest
    if dist_v.len() > circ_rad:
        return Position(0, 0)
    if dist_v.len() <= 0:
        raise(ValueError, "Circle's center is exactly on segment")
    offset = dist_v / dist_v.len() * (circ_rad - dist_v.len())
    return offset

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))