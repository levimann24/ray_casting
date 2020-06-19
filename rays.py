import pygame
import math


class Rays:
    def __init__(self, main):
        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = main.screen_rect
        self.color = self.settings.r_color
        self.length = self.settings.r_length

        self.center = self.screen_rect.center
        self.ray_end_points = []

        # create all of the ray directions
        for a in range(0, 360, self.settings.deg_diff):
            end_point = (self.length * math.cos(math.radians(a))+self.center[0],
                         self.length*math.sin(math.radians(a))+self.center[1])
            self.ray_end_points.append(end_point)
        print(len(self.ray_end_points))

    def draw_center(self):
        pygame.draw.circle(self.screen, self.color,
                           self.screen_rect.center, 10)

    def draw_rays(self):
        for ray in self.ray_end_points:
            pygame.draw.line(self.screen, self.color, self.center, ray)
