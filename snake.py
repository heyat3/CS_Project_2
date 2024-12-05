#https://youtu.be/ebVV-6QMUIU?si=-31a_nAUGqT5aBsc
#used video above

import pygame
from sys import exit
import random

#setup
pygame.init()

screen_width = 600
screen_height = 600
block_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#player = pygame.Rect(300, 300, 20, 20)

class Snake:
    def __init__(self):
        self.x, self.y = block_size, block_size
        self.dirX = 1
        self.dirY = 0
        self.head = pygame.Rect(self.x, self.y, block_size, block_size)
        self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]
        self.dead = False

    def update(self):
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, screen_width) or self.head.y not in range(0, screen_height):
                self.dead = True

            if self.dead:
                '''change this to go to game over screen'''
                self.x, self.y = block_size, block_size
                self.head = pygame.Rect(self.x, self.y, block_size, block_size)
                self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]
                self.dirX = 1
                self.dirY = 0
                self.dead = False
                apple = Apple()

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.dirX * block_size
        self.head.y += self.dirY * block_size
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, screen_width)//block_size - 1) * block_size
        self.y = int(random.randint(0, screen_height)//block_size - 1) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)

    def update(self):
        pygame.draw.rect(screen, 'Red', self.rect)

"""button class from: https://github.com/baraltech/Menu-System-PyGame/blob/main/button.py"""
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

def drawGrid():
    for x in range(0, screen_width, block_size):
        for y in range(0, screen_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, '#2b2b2b', rect, 1)

def get_font(size):
    return pygame.font.Font('Comic Sans MS.ttf', size)

def play():
    snake = Snake()
    apple = Apple()
    score = len(snake.body) + 1 #will be in on top of screen and in stats at end of game

    while True:
        screen.fill('Black')
        drawGrid()
        pygame.display.set_caption('Snake Game')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    snake.dirY = 1
                    snake.dirX = 0
                elif event.key == pygame.K_w:
                    snake.dirY = -1
                    snake.dirX = 0
                elif event.key == pygame.K_a:
                    snake.dirY = 0
                    snake.dirX = -1
                elif event.key == pygame.K_d:
                    snake.dirY = 0
                    snake.dirX = 1


        snake.update()
        apple.update()

        pygame.draw.rect(screen, '#d9d9d9', snake.head)

        for square in snake.body:
            pygame.draw.rect(screen, '#d9d9d9', square)

        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, block_size, block_size))
            apple = Apple()

        pygame.display.update()
        clock.tick(10) #changes speed --> will be dependent on user input

def main_menu():
    pygame.display.set_caption('Snake Menu')
    font = pygame.font.Font('Comic Sans MS.ttf', 74)
    small_font = pygame.font.Font('Comic Sans MS.ttf', 50)

    menu_options = ['Start', 'Options', 'Quit']

    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill('Black')
        title_text = get_font(75).render("Main Menu", True, 'White')
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))

        pygame.display.flip()
        #play()
        menu_play = Button(image=None, pos=(200, 200), text_input='START', font=get_font(50), base_color='White', hovering_color='Gray')
        menu_play.changeColor(mouse_pos)
        menu_play.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_play.checkForInput(mouse_pos):
                    play()


        pygame.display.update()

def game_over():
    while True:
        screen.fill('Black')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

main_menu()
#drawGrid()
pygame.quit()