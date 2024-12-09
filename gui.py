import pygame
from snake import Snake
import logic

def drawGrid():
    for x in range(0, Snake.get_screen_w(), Snake.get_block_size()):
        for y in range(0, Snake.get_screen_h(), Snake.get_block_size()):
            rect = pygame.Rect(x, y, Snake.get_block_size(), Snake.get_block_size())
            pygame.draw.rect(logic.screen, '#2b2b2b', rect, 1)