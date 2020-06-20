class Settings:
    def __init__(self):
        """Initialize the settings"""
        # SCREEN SETTINGS
        self.WIDTH = 900
        self.HEIGHT = 900
        self.bg_color = (100, 100, 100)

        # boundary settings
        self.bound_color = (255, 255, 255)
        self.bound_width = 2
        self.n_boundaries = 5

        # ray settings
        self.deg_diff = 3
        self.r_color = (100, 0, 0)
        self.r_length = 10
