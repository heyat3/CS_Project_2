import pygame
import random
from logic import *

class Apple:
    def __init__(self, snake, screen):
        """
        initialize Apple object

        :param snake: Snake object to make sure apple doesn't spawn on snake
        :param screen: surface where apple is drawn
        """
        self.screen: pygame.Surface = screen
        self.x: int = int(random.randint(0, Snake.get_screen_w(self=snake))//Snake.get_block_size(self=snake) - 1) * Snake.get_block_size(self=snake)
        self.y: int = int(random.randint(0, Snake.get_screen_h(self=snake)//Snake.get_block_size(self=snake) - 1) * Snake.get_block_size(self=snake))
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, Snake.get_block_size(self=snake), Snake.get_block_size(self=snake))

    def update(self):
        """
        draws apple on screen

        :return: None
        """
        pygame.draw.rect(self.screen, 'Red', self.rect)
