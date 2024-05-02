import pygame as py
from colors import *

class HashScreen:
    def __init__(self, font) -> None:
        self.font = py.font.Font(font, 30)
        self.input_rect = py.Rect(50, 50, 700, 50)
        self.output_rect = py.Rect(50, 150, 700, 50)
        self.output_text = []
        self.input_text = ''
        self.placeholder_text = ''
        self.input_active = False

    def draw(self, screen):
        screen.fill(WHITE)

        # Input box
        self.input_rect.center = screen.get_rect().center
        self.input_rect.y -= 80
        py.draw.rect(screen, UCA_BLUE, self.input_rect, 2)
        input_surface = self.font.render(self.input_text, True, UCA_BLUE)
        input_surface_rect = input_surface.get_rect()
        input_surface_rect.midleft = self.input_rect.midleft
        input_surface_rect.x += 10
        screen.blit(input_surface, input_surface_rect)

        # Output box
        self.output_rect.center = screen.get_rect().center
        self.output_rect.y += 50
        py.draw.rect(screen, UCA_BLUE, self.output_rect, 2)
        for text in self.output_text:
            text_surface = self.font.render(text, True, UCA_BLUE)
            text_surface_rect = text_surface.get_rect()
            text_surface_rect.midleft = self.output_rect.midleft
            text_surface_rect.x += 10
            screen.blit(text_surface, text_surface_rect)

    def handle_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            self.input_active = self.input_rect.collidepoint(event.pos)
        if event.type == py.KEYDOWN:
            if self.input_active:
                if event.key == py.K_RETURN:
                    if self.input_text.strip() != '':
                        self.output_text = []
                        self.output_text.append(self.input_text.strip() + " | " + self.get_hash_value(self.input_text.strip()))
                        self.input_text = ''
                elif event.key == py.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode
        return self

    def get_hash_value(self, value):
        hash_value = 0

        for char in value:
            hash_value += ord(char)

        return str(hash_value % 101)
