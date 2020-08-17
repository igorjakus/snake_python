import sys
import pygame

from settings import Settings
from snake import Snake, Apple


class SnakeGame:

	def __init__(self):

		# Screen initialization
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(self.settings.window)
		pygame.display.set_caption(self.settings.screen_caption)

		# Game mechanism
		self.delta = 0.0
		self.game_over = False
		self.clock = pygame.time.Clock()

		# Creation of objects
		self.snake = Snake(self)
		self.apple = Apple(self)

	def run_game(self):
		while not self.game_over:
			self.delta += self.clock.tick() / 1000.0
			while self.delta > 1 / 20.0:
				self._check_events()
				self.snake.move()
				#if self.snake.check_lose():
				#	self.game_over == True
				self.snake.check_apple(self.apple)
				self._update_screen()
				self.delta = 0.0
			


	def _check_events(self):
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			# Input
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				self.snake.change_direction('up')
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				self.snake.change_direction('down')
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				self.snake.change_direction('left')
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				self.snake.change_direction('right')
			
	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.snake.blitme()
		self.apple.blitme()

		pygame.display.flip()


if __name__ == '__main__':
	# Running a copy of the game
	snake = SnakeGame()
	snake.run_game()