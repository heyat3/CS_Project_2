import pygame
from snake import Snake
#import logic

def drawGrid(snake):
    """
    draws grid for the game

    :param snake: to make the squares the same dimensions as the snake
    :return: None
    """
    screen: pygame.Surface = pygame.display.set_mode((Snake.get_screen_w(self=snake), Snake.get_screen_h(self=snake)))

    for x in range(0, Snake.get_screen_w(self=snake), Snake.get_block_size(self=snake)):
        for y in range(0, Snake.get_screen_h(self=snake), Snake.get_block_size(self=snake)):
            rect: pygame.Rect = pygame.Rect(x, y, Snake.get_block_size(self=snake), Snake.get_block_size(self=snake))
            pygame.draw.rect(screen, '#2b2b2b', rect, 1)