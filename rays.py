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
            end_point = [self.length * math.cos(math.radians(a))+self.center[0],
                         self.length*math.sin(math.radians(a))+self.center[1], 1000]
            self.ray_end_points.append(end_point)

    def get_intersection(self, boundary1, boundary2):
        for ray in self.ray_end_points:
            # t units
            x1 = boundary1[0]
            y1 = boundary1[1]
            x2 = boundary2[0]
            y2 = boundary2[1]

            # u units
            x3 = self.center[0]
            y3 = self.center[1]
            x4 = ray[0]
            y4 = ray[1]

            denomonator = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
            if denomonator == 0:
                return
            # find t
            numt = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
            t = numt/denomonator
            # find u
            numu = (x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)
            u = -numu/denomonator
            if t >= 0 and t <= 1 and u >= 0:
                px = (x3+u*(x4-x3))
                py = (y3+u*(y4-y3))
                d = math.sqrt((x3-px)**2+(y3-py)**2)
                if d < ray[2]:
                    ray[2] = d
                    ray[0] = px
                    ray[1] = py
                else:
                    break

    def draw_center(self):
        pygame.draw.circle(self.screen, self.color,
                           self.center, 10)

    def draw_rays(self):
        for ray in self.ray_end_points:
            pygame.draw.line(self.screen, self.color,
                             self.center, (ray[0], ray[1]))

    def get_center(self):
        self.center = pygame.mouse.get_pos()
        self.reset_rays()

    def reset_rays(self):
        i = 0
        for a in range(0, 360, self.settings.deg_diff):
            self.ray_end_points[i] = [self.length * math.cos(math.radians(a))+self.center[0],
                                      self.length*math.sin(math.radians(a))+self.center[1], 1000]
            i += 1
