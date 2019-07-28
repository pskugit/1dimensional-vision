import sys
import numpy
import pygame
import random

from eye import *
from ray import *
from util import *
from creature import *
from boundary import *
from geometrics import *


#initialization
pygame.init()
clock = pygame.time.Clock()

bg_color = (51,51,51)
window = pygame.display.set_mode((MAP_WIDTH,MAP_HEIGHT+VIEW_HEIGHT))
pygame.display.set_caption("Ray casting")
window.fill(bg_color)

f = Frame(0, 0, MAP_WIDTH,MAP_HEIGHT)
walls = list(f.get_boundaries())
scene = []
for i in range(10):
    scene.append(Boundary(random.randint(0,MAP_WIDTH),random.randint(0,MAP_HEIGHT),random.randint(0,MAP_WIDTH),random.randint(0,MAP_HEIGHT)))
#scene.extend(walls)

#
# CHANGE CHARACTER HERE
#
char = Creature(Position(200,200), window)
#char = Cyclops(Position(200,200), window)

pressed_w = False
pressed_a = False
pressed_s = False
pressed_d = False
pressed_up = False
pressed_left = False
pressed_down = False
pressed_right = False

while True:
    window.fill(bg_color)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            char.move(Position(*mouse_pos))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pressed_w = True
            elif event.key == pygame.K_a:
                pressed_a = True
            elif event.key == pygame.K_s:
                pressed_s = True
            elif event.key == pygame.K_d:
                pressed_d = True
            if event.key == pygame.K_UP:
                pressed_up = True
            elif event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_DOWN:
                pressed_down = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
        elif event.type == pygame.KEYUP:  # check for key releases
            if event.key == pygame.K_w:
                pressed_w = False
            elif event.key == pygame.K_a:
                pressed_a = False
            elif event.key == pygame.K_s:
                pressed_s = False
            elif event.key == pygame.K_d:
                pressed_d = False
            if event.key == pygame.K_UP:
                pressed_up = False
            elif event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_DOWN:
                pressed_down = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
    #character movement
    if pressed_w:
        char.forward()
    if pressed_a:
        char.rotate(0.1)
    if pressed_s:
        char.backward()
    if pressed_d:
        char.rotate(-0.1)
    if pressed_up:
        pass
    if pressed_left:
        pass
    if pressed_down:
        pass
    if pressed_right:
        pass

    #render character
    char.scene = scene
    char.show()

    #render obstacles
    for elemet in scene:
        elemet.show(window)

    #render images
    char.see()

    #pygame.time.delay(90)
    pygame.display.update()
    clock.tick(30)

