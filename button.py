"""button class from: https://github.com/baraltech/Menu-System-PyGame/blob/main/button.py
   video: https://www.youtube.com/watch?v=GMBqjxcKogA"""
import pygame


class Button:
    def __init__(self, image: pygame.Surface, pos: tuple[int, int], text_input: str, font: pygame.font.Font, base_color: str, hovering_color: str):
        """
        initializes button with image, position, text, font and color

        :param image: image displayed as the button's background (or None for text-only button)
        :param pos: position of button's center (x, y)
        :param text_input: text displayed on the button
        :param font: font used to render button's text
        :param base_color: default color of button's text
        :param hovering_color: color of button's text when hovered over
        """
        self.image: pygame.Surface = image
        self.x_pos: int = pos[0]
        self.y_pos: int = pos[1]
        self.font: pygame.font.Font = font
        self.base_color: str = base_color
        self.hovering_color: str = hovering_color
        self.text_input: str = text_input
        self.text:pygame.Surface = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.text

        self.rect: pygame.Rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect: pygame.Rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """
        renders button image and text on screen

        :param screen: screen to render button
        :return None:
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position: tuple[int, int]):
        """
        check if position is in button bounds

        :param position: (x, y) position to check
        :return bool: True if within bounds, False otherwise
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        """
        change button text color if hovered over

        :param position: (x, y) position of mouse
        :return None:
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text: pygame.Surface = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)