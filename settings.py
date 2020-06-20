class Settings:
    def __init__(self):
        """Initialize the settings"""
        # SCREEN SETTINGS
        self.WIDTH = 1400
        self.HEIGHT = 1000
        self.bg_color = (0, 0, 0)

        # boundary settings
        self.bound_color = (255, 255, 255)
        self.bound_width = 1
        self.n_boundaries = 3

        # ray settings
        self.deg_diff = 3
        self.r_color = (200, 0, 0)
        self.r_length = 2000
