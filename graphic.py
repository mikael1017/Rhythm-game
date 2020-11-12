import os
import pygame
current_path = os.path.dirname(__file__)    # current file path
image_path = os.path.join(current_path, "images")

class Notebar(object):
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = -40
        self.image = pygame.image.load(os.path.join(image_path, "bar.png"))
    def set_y(self, y):
        self.y_pos = y

    def get_x(self):
        return int(self.x_pos)

    def get_y(self):
        return int(self.y_pos)

    def default(self):
        self.set_y(-40)

    def get_image(self):
        return self.image

class Path(object):
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 30
        self.image = pygame.image.load(os.path.join(image_path, "barpath.png"))
    
    def get_x(self):
        return self.x_pos

    def get_y(self):
        return self.y_pos

    def get_image(self):
        return self.image

    def entered(self):
        self.image = pygame.image.load(os.path.join(image_path, "barpathEntered.png"))

    def default(self):
        self.image = pygame.image.load(os.path.join(image_path, "barpath.png"))
