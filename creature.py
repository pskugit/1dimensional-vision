import pygame
import numpy as np
from ray import *
from util import *
from image import Image
from eye import Eye

class Cyclops():
    def __init__(self, position, window):
        self.window = window
        self.position = position
        self.size = 10
        self.view_angle = 0
        self.eye = Eye(self.position)
        self.eye.color = BLUE
        self.color = WHITE
        self.speed = 4

    def move(self, position):
        for element in self.scene:
            #on_line = (-3 < (distance(element.a, position) + distance(position, element.b) - distance(element.a, element.b)) < 3)
            if False:
                print("collision")
                return
            else:
                self.position.translate_to(position)

    def forward(self):
        direction = Position(
            math.sin(self.view_angle),
            math.cos(self.view_angle))
        direction = direction.multipy(self.speed)
        self.move(self.position.plus(direction))

    def backward(self):
        direction = Position(
            math.sin(self.view_angle),
            math.cos(self.view_angle))
        direction = direction.multipy(self.speed)
        self.move(self.position.minus(direction))

    def rotate(self, direction):
        self.eye.view_angle += direction
        self.view_angle += direction


    def show(self):

        #pygame.draw.circle(window, self.color, self.position.toTuple(), self.size, 1)
        self.eye.show(self.window)

        lineEnd = (self.position.x + math.sin(self.view_angle) * (self.size - 2),
                   self.position.y + math.cos(self.view_angle) * (self.size - 2))
        pygame.draw.line(self.window, (255, 255, 255), self.position.toTuple(), lineEnd, 2)

    def see(self):
        self.eye.update()
        self.eye.see(self.scene)
        self.render()

    def render(self):

        render = Image(self.eye.rays)
        render.draw2D(Position(0, MAP_HEIGHT), self.window)

        #left_img.draw(Position(0, 0), self.window)
        #show_text("left eye", self.window, Position(3, 3))



class Creature():
    def __init__(self, position, window):
        self.window = window
        self.position = position
        self.size = 20
        self.view_angle = 0
        self.left_eye_pos = Position(self.position.x+20,self.position.y)
        self.right_eye_pos = Position(self.position.x-20,self.position.y)

        self.left_eye = Eye(self.left_eye_pos)
        self.right_eye = Eye(self.right_eye_pos)
        self.left_eye.color = BLUE
        self.color = WHITE
        self.speed = 4
        self.scene = []

    def move(self, position):
        for element in self.scene:
            #on_line = (-3 < (distance(element.a, position) + distance(position, element.b) - distance(element.a, element.b)) < 3)
            if False:
                print("collision")
                return
            else:
                self.position.translate_to(position)

    def forward(self):
        direction = Position(
            math.sin(self.view_angle),
            math.cos(self.view_angle))
        direction = direction.multipy(self.speed)
        self.move(self.position.plus(direction))
        self.left_eye_pos.translate_to(self.left_eye_pos.plus(direction))
        self.right_eye_pos.translate_to(self.right_eye_pos.plus(direction))

    def backward(self):
        direction = Position(
            math.sin(self.view_angle),
            math.cos(self.view_angle))
        direction = direction.multipy(self.speed)
        self.move(self.position.minus(direction))
        self.left_eye_pos.translate_to(self.left_eye_pos.minus(direction))
        self.right_eye_pos.translate_to(self.right_eye_pos.minus(direction))

    def place_eye(self):
        return

    def rotate(self, direction):
        self.left_eye.view_angle += direction
        self.right_eye.view_angle += direction
        self.view_angle += direction

        new_left = Position(self.position.x + self.size * math.cos(self.view_angle), self.position.y - self.size *math.sin(self.view_angle))
        self.left_eye_pos.translate_to(new_left)
        new_right = Position(self.position.x - self.size * math.cos(self.view_angle), self.position.y + self.size *math.sin(self.view_angle))
        self.right_eye_pos.translate_to(new_right)


    def show(self):
        pygame.draw.circle(self.window, self.color, self.position.toTuple(), self.size, 1)

        self.left_eye.show(self.window)
        self.right_eye.show(self.window)


    def see(self):
        self.left_eye.update()
        self.left_eye.see(self.scene)
        left_img = self.left_eye.get_image()
        left_img.draw1D(Position(0, MAP_HEIGHT+VIEW_HEIGHT-60), self.window)
        show_text("left eye", self.window, Position(3, MAP_HEIGHT+VIEW_HEIGHT-54))

        self.right_eye.update()
        self.right_eye.see(self.scene)
        right_img = self.right_eye.get_image()
        right_img.draw1D(Position(0, MAP_HEIGHT+VIEW_HEIGHT-30), self.window)
        show_text("right eye",self.window,Position(3, MAP_HEIGHT+VIEW_HEIGHT-24))

