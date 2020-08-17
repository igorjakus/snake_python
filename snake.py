from settings import Settings
import pygame
import random

DIRECT_DICT = {"left" : (-20, 0), "right" : (20, 0),
			"up" : (0, -20), "down" : (0, 20), None: (0, 0)}

OPPOSITES = {"left" : "right", "right" : "left",
			"up" : "down", "down" : "up"}

class Square:
	def __init__(self, x, y):
		self.settings = Settings()
		self.rect_size = self.settings.rect_size 
		self.color = self.settings.snake_color
		self.x = x
		self.y = y

class Snake:

	def __init__(self, snake_game):
		self.screen_rect = snake_game.screen.get_rect()
		self.screen = snake_game.screen
		self.body = [Square(400, 400)]
		self.after_eating = False
		self.direction = None
		
	def blitme(self):
		for part in self.body:
			pygame.draw.rect(self.screen, part.color, 
				(part.x, part.y, part.rect_size, part.rect_size))

	def change_direction(self, direction):
		self.direction = direction

	def move(self):

		# temporal position of last element
		tempx = self.body[-1].x
		tempy = self.body[-1].y

		# moving all snake parts
		for index in reversed(range(1, len(self.body))):
			self.body[index].x = self.body[index-1].x
			self.body[index].y = self.body[index-1].y

		# appending new snake part
		if self.after_eating:
			self.after_eating = False
			self.body.append(Square(tempx, tempy))

		#moving the head
		x, y = DIRECT_DICT[self.direction]
		self.body[0].x += x
		self.body[0].y += y

	def check_lose(self):
		for part in self.body[1:]:
			# check collidation with himself
			if part.x == self.body[0].x or part.y == self.body[0].y:
				return True

		# check collidation with screen
		if part.x >= 800 or part.y >= 800 or part.x <= 0 or part.y <= 0:
			return True
		else: 
			return False

	
	def check_apple(self, apple):
		# eat an apple if head pos is the same as apple pos
		x, y = self.body[0].x, self.body[0].y
		if x == apple.x and y == apple.y:
			self.after_eating = True
			self.move()
			apple.move()
		
class Apple:
	def __init__(self, snake_game):
		self.screen = snake_game.screen
		self.screen_rect = snake_game.screen.get_rect()

		self.settings = Settings()
		self.x = random.randint(0, (self.settings.window[0] - 20) / 20) * 20
		self.y = random.randint(0, (self.settings.window[1] - 20) / 20) * 20
		self.rect_size = self.settings.rect_size
		self.color = self.settings.apple_color

	def blitme(self):
		pygame.draw.rect(self.screen, self.color, 
			(self.x, self.y, self.rect_size, self.rect_size))

	def move(self):
		self.x = random.randint(0, (self.settings.window[0] - 20) / 20) * 20
		self.y = random.randint(0, (self.settings.window[1] - 20) / 20) * 20

	

