import pygame
import logic

class Snake:
    def __init__(self):
        self.__screen_width = 600
        self.__screen_height = 600
        self.__block_size = 20

        self.x, self.y = self.__block_size, self.__block_size
        self.dirX = 1
        self.dirY = 0
        self.head = pygame.Rect(self.x, self.y, self.__block_size, self.__block_size)
        self.body = [pygame.Rect(self.x - self.__block_size, self.y, self.__block_size, self.__block_size)]
        self.dead = False

    def update(self):
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, self.__screen_width) or self.head.y not in range(0, self.__screen_height):
                self.dead = True

            if self.dead:
                self.dirX = 0
                self.dirY = 0
                logic.screen.fill('Black')
                logic.game_over()

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.dirX * self.__block_size
        self.head.y += self.dirY * self.__block_size
        self.body.remove(self.head)

    def get_screen_w(self):
        return self.__screen_width

    def get_screen_h(self):
        return self.__screen_height

    def get_block_size(self):
        return self.__block_size
