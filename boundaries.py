import pygame
import random


class Boundary:
    def __init__(self, main):
        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = main.screen_rect
        self.width = self.settings.bound_width
        self.color = self.settings.bound_color
        self.x1 = random.randint(0, self.settings.WIDTH)
        self.y1 = random.randint(0, self.settings.HEIGHT)
        self.x2 = random.randint(0, self.settings.WIDTH)
        self.y2 = random.randint(0, self.settings.HEIGHT)
        self.start_pos = (self.x1, self.y1)
        self.end_pos = (self.x2, self.y2)

    def draw_line(self, start=(0, 0), end=(0, 0)):
        if start == (0, 0) and end == (0, 0):
            pygame.draw.line(self.screen, self.color,
                             self.start_pos, self.end_pos, self.width)
        else:
            pygame.draw.line(self.screen, self.color, start, end, self.width)
