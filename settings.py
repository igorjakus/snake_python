class Settings:
    def __init__(self):
        # Game settings
        self.game_speed = 1.0

        self.snake_color = (50, 205, 50)  # limegreen
        self.apple_color = (178, 34, 34)  # firebrick
        self.unit = 20  # one square size

        self.window = (self.unit * 40, self.unit * 40)
        self.bg_color = (0, 0, 0)
