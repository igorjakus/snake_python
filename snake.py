from settings import Settings
import pygame
import random

unit = Settings().unit

DIRECT_DICT = {"left" : (-unit, 0), "right" : (unit, 0),
			"up" : (0, -unit), "down" : (0, unit), None: (0, 0)}

OPPOSITES = {"left" : "right", "right" : "left",
			"up" : "down", "down" : "up"}


class Square:
	def __init__(self, x = unit*19, y = unit*19):
		self.settings = Settings()
		self.unit = unit
		self.color = self.settings.snake_color
		self.x = x
		self.y = y

class Snake:

	def __init__(self, snake_game):
		self.screen_rect = snake_game.screen.get_rect()
		self.screen = snake_game.screen
		self.body = [ Square() ]
		self.after_eating = False
		self.direction = None
		
	def blitme(self):
		for part in self.body:
			pygame.draw.rect(self.screen, part.color, 
				(part.x, part.y, unit, unit))

	def change_direction(self, direction):
		self.direction = direction

	def move(self):

		tempx = self.body[-1].x
		tempy = self.body[-1].y

		if self.direction:
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

		# check collision with himself
		for part in self.body[1:]:
			if part.x == self.body[0].x or part.y == self.body[0].y:
				return True

		# check collision with screen
		if self.body[0].x > unit*39 or self.body[0].y > unit*39 or self.body[0].x < 0 or self.body[0].y < 0:
			return True
		else: 
			return False

	def check_apple(self, apple):
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
		self.x, self.y = self.rand_pos()
		self.color = self.settings.apple_color

	def blitme(self):
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, unit, unit))

	def move(self):
		self.x, self.y = self.rand_pos()

	def rand_pos(self):
		return random.randint(0, 39) * unit, random.randint(0, 39) * unit
