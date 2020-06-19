import pygame
import sys
import settings
import boundaries
import rays


class RayCast:
    """Let's make a ray cast program"""

    def __init__(self):
        self.settings = settings.Settings()
        self.s_width = self.settings.WIDTH
        self.s_height = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color

        # initalize the screen
        self.screen = pygame.display.set_mode((self.s_width, self.s_height))
        pygame.display.set_caption("Ray Casting Demo")
        self.screen_rect = self.screen.get_rect()

        # initialize boundary array
        self.boundary_list = []
        self._create_boundaries()

        # Initialize boundaries at each wall
        self.b_top = boundaries.Boundary(self)
        self.b_right = boundaries.Boundary(self)
        self.b_left = boundaries.Boundary(self)
        self.b_bottom = boundaries.Boundary(self)

        # create rays
        self.ray = rays.Rays(self)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def on_loop(self):
        pass

    def on_render(self):
        # draw the screen
        self.screen.fill(self.bg_color)
        # draw the wall boundaries
        self.b_top.draw_line((0, -1), (self.s_width, -1))
        self.b_right.draw_line(
            (self.s_width, 0), (self.s_width, self.s_height))
        self.b_bottom.draw_line(
            (0, self.s_height), (self.s_width, self.s_height))
        self.b_left.draw_line((-1, 0), (-1, self.s_height))
        # draw the boundaries
        for boundary in self.boundary_list:
            boundary.draw_line()

        # draw the center of the rays
        self.ray.draw_center()
        # draw the rays
        self.ray.draw_rays()
        # update the screen
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
# ---------------------------------------------------

    def _create_boundaries(self):
        while len(self.boundary_list) < self.settings.n_boundaries:
            boundary = boundaries.Boundary(self)
            self.boundary_list.append(boundary)


if __name__ == "__main__":
    rc = RayCast()
    rc.on_execute()
