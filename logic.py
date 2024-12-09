#https://youtu.be/ebVV-6QMUIU?si=-31a_nAUGqT5aBsc
#used video above - GitHub link below
#https://github.com/harsitbaral/Snake/blob/main/main.py


import pygame
from sys import exit
from snake import Snake
from button import Button
from apple import Apple
import gui

#setup
pygame.init()

screen = pygame.display.set_mode((Snake.get_screen_w(), Snake.get_screen_h()))
clock = pygame.time.Clock()

#player = pygame.Rect(300, 300, 20, 20)


def get_font(size):
    return pygame.font.Font('Comic Sans MS.ttf', size)

def play():
    global score

    snake = Snake()
    apple = Apple()
    score = len(snake.body) + 1 #will be in on top of screen and in stats at end of game

    while True:
        screen.fill('Black')
        gui.drawGrid()
        pygame.display.set_caption('Snake - Game')


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
            snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, Snake.get_block_size(), Snake.get_block_size()))
            apple = Apple()

        pygame.display.update()
        clock.tick(10) #changes speed --> will be dependent on user input

def main_menu():
    pygame.display.set_caption('Snake - Menu')
    '''font = pygame.font.Font('Comic Sans MS.ttf', 74)
    small_font = pygame.font.Font('Comic Sans MS.ttf', 50)

    menu_options = ['Start', 'Options', 'Quit']'''

    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill('Black')
        title_text = get_font(75).render("Main Menu", True, 'White')
        screen.blit(title_text, (Snake.get_screen_w() // 2 - title_text.get_width() // 2, 100))

        pygame.display.flip()
        #play()
        menu_play = Button(image=None, pos=(250, 400), text_input='START', font=get_font(50), base_color='White', hovering_color='Gray')
        menu_play.changeColor(mouse_pos)
        menu_play.update(screen)

        #quit
        menu_quit = Button(image=None, pos=(250, 500), text_input='EXIT', font=get_font(50), base_color='White',
                           hovering_color='Gray')
        menu_quit.changeColor(mouse_pos)
        menu_quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_play.checkForInput(mouse_pos):
                    play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_quit.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

def game_over():
    global score

    pygame.display.set_caption('Snake - Game Over')
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill('Black')

        #game over text
        game_over_text = get_font(75).render("Game Over!", True, 'White')
        screen.blit(game_over_text, (Snake.get_screen_w() // 2 - game_over_text.get_width() // 2, 100))

        #score
        score_text = get_font(40).render(f"Score: {score}", True, 'White')
        screen.blit(score_text, (Snake.get_screen_w() // 2 - score_text.get_width() // 2, 200))

        pygame.display.flip()

        #menu button
        over_menu = Button(image=None, pos=(300, 300), text_input='MAIN MENU', font=get_font(50), base_color='White',
                           hovering_color='Gray')
        over_menu.changeColor(mouse_pos)
        over_menu.update(screen)

        #quit button
        over_quit = Button(image=None, pos=(400, 350), text_input='EXIT', font=get_font(50), base_color='White',
                           hovering_color='Gray')
        over_quit.changeColor(mouse_pos)
        over_quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if over_quit.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

                if over_menu.checkForInput(mouse_pos):
                    main_menu()

        pygame.display.update()


main_menu()
#drawGrid()
pygame.quit()