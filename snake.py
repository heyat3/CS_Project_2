import pygame
from pygame.rect import RectType

import logic

class Snake:
    def __init__(self):
        """
        initialize Snake object

        :return: None
        """
        self.screen_width: int = 600
        self.screen_height: int = 600
        self.block_size: int = 20

        self.x: int = self.block_size
        self.y: int = self.block_size
        self.dirX: int = 1
        self.dirY: int = 0
        self.head: pygame.Rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        self.body: list[pygame.Rect] = [pygame.Rect(self.x - self.block_size, self.y, self.block_size, self.block_size)]
        self.dead: bool = False

    def update(self):
        """
        update snake position and check for collision with self or boundaries
        if snake dies, game_over() is called

        :return: None
        """
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, self.screen_width) or self.head.y not in range(0, self.screen_height):
                self.dead = True

            if self.dead:
                self.dirX = 0
                self.dirY = 0
                logic.screen.fill('Black')
                logic.game_over()

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.dirX * self.block_size
        self.head.y += self.dirY * self.block_size
        self.body.remove(self.head)


    def get_screen_w(self) -> int:
        """
        get width of screen

        :return int: width of screen
        """
        return self.screen_width

    @staticmethod
    def get_screen_h(self) -> int:
        """
        get height of screen

        :return int: height of screen
        """
        return self.screen_height

    @staticmethod
    def get_block_size(self) -> int:
        """
        get block size

        :return int: block size
        """
        return self.block_size
