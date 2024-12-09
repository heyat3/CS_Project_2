import pygame
import random
from snake import Snake
import logic

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, Snake.get_screen_w())//Snake.get_block_size() - 1) * Snake.get_block_size()
        self.y = int(random.randint(0, Snake.get_screen_h())//Snake.get_block_size() - 1) * Snake.get_block_size()
        self.rect = pygame.Rect(self.x, self.y, Snake.get_block_size(), Snake.get_block_size())

    def update(self):
        pygame.draw.rect(logic.screen, 'Red', self.rect)
