class Settings:
	def __init__(self):
		
		# Squares settins
		self.snake_color = (50, 205, 50) # limegreen
		self.apple_color = (178,34,34) # firebrick
		self.unit = 20 # one square size 
		
		# Screen settings
		self.screen_caption = "Snake Game - Python 3, Igor Jakus"
		self.window = (self.unit * 40, self.unit * 40) # pixels width and length
		self.bg_color = (0, 0, 0) # black

		