import sys
import pygame

from settings import Settings
from snake import Snake, Apple

KEYBOARD = {
	pygame.K_w: 'up',
	pygame.K_UP: 'up',
	
	pygame.K_a: 'left',
	pygame.K_LEFT: 'left',
	
	pygame.K_d: 'right',
	pygame.K_RIGHT: 'right',
	
	pygame.K_s: 'down',
	pygame.K_DOWN: 'down',

	pygame.K_SPACE: None, 
}


class SnakeGame:

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(self.settings.window)
		pygame.display.set_caption(self.settings.screen_caption)

		self.delta = 0.0
		self.game_over = False
		self.clock = pygame.time.Clock()

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
				#	break
				self.snake.check_apple(self.apple)
				self._update_screen()
				self.delta = 0.0
			

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.handle_quit(event)

			elif event.type == pygame.KEYDOWN:
				self.handle_keydown(event)

	def handle_quit(self, event):
		sys.exit()

	def handle_keydown(self, event):
		if event.key in KEYBOARD:
			self.snake.change_direction(KEYBOARD[event.key])

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.snake.blitme()
		self.apple.blitme()
		pygame.display.flip()


if __name__ == '__main__':
	snake = SnakeGame()
	snake.run_game()