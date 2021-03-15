from settings import Settings
from random import randint
import pygame

unit = Settings().unit

DIRECT_DICT = {"left": (-unit, 0), "right": (unit, 0),
               "up": (0, -unit), "down": (0, unit)}

OPPOSITES = {"left": "right", "right": "left",
             "up": "down", "down": "up"}


class Square:
    def __init__(self, x=unit * 19, y=unit * 19):
        self.unit = Settings().unit
        self.color = Settings().snake_color
        self.x = x
        self.y = y


class Snake:

    def __init__(self, snake_game):
        self.screen_rect = snake_game.screen.get_rect()
        self.screen = snake_game.screen
        self.body = [Square()]
        self.after_eating = False
        self.direction = "up"

    def reset(self):
        self.body = [Square()]
        
    def blitme(self):
        for part in self.body:
            pygame.draw.rect(self.screen, part.color,
                             (part.x, part.y, unit, unit))

    def change_direction(self, direction):
        if len(self.body) > 1:
            if self.direction != OPPOSITES[direction]:
                self.direction = direction
                return True
            else:
                return False
        else:
            self.direction = direction
            return True

    def move(self):
        x, y = self.body[-1].x, self.body[-1].y

        if self.direction:
            # moving all snake parts
            for index in reversed(range(1, len(self.body))):
                self.body[index].x = self.body[index - 1].x
                self.body[index].y = self.body[index - 1].y

        # appending new snake part
        if self.after_eating:
            self.after_eating = False
            self.body.append(Square(x, y))

        # moving the head
        x, y = DIRECT_DICT[self.direction]
        self.body[0].x += x
        self.body[0].y += y

    def check_lose(self):
        # check collision with himself
        if not self.after_eating:
            for part in self.body[1:]:
                if part.x == self.body[0].x and part.y == self.body[0].y:
                    return True
        
        # check collision with screen
        x, y = self.body[0].x, self.body[0].y
        if x < 0 or y < 0 or x > unit * 39 or y > unit * 39:
            return True
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
        self.x, self.y = self.rand_pos()
        self.color = Settings().apple_color

    def blitme(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.x, self.y, unit, unit))

    def move(self):
        self.x, self.y = self.rand_pos()

    @staticmethod
    def rand_pos():
        return randint(0, 39) * unit, randint(0, 39) * unit
