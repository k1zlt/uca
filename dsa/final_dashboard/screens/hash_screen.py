import pygame as py
from colors import *

class HashScreen:
    def __init__(self, font, main_menu) -> None:
        self.font = py.font.Font(font, 36)
        self.input_rect = py.Rect(50, 50, 700, 50)
        self.output_rect = py.Rect(50, 150, 700, 400)
        self.back_button = py.Rect(50, 0, 100, 50)

        self.output_text = []
        self.input_text = ''
        self.placeholder_text = 'Enter a value: '
        self.input_active = False
        self.input_text_surface = self.font.render(self.input_text, True, BLACK)
        self.input_color = INPUT_COLOR
        self.unfocused_color = INPUT_UNFOCUSED_COLOR  
        self.input_active_bg_color = INPUT_BG_COLOR
        self.input_unfocused_bg_color = INPUT_UNFOCUSED_BG_COLOR
        self.main_menu = main_menu
    
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        if self.input_active:
            py.draw.rect(screen, INPUT_BG_COLOR, self.input_rect)
        else:
            py.draw.rect(screen, INPUT_UNFOCUSED_BG_COLOR, self.input_rect)

        if not self.input_text.strip():
            text_surface = self.font.render(self.placeholder_text, True, self.unfocused_color)
        else:
            text_surface = self.font.render(self.input_text.strip(), True, UCA_BLUE)
        
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.left = self.input_rect.left + 5
        text_surface_rect.centery = self.input_rect.centery
        screen.blit(text_surface, text_surface_rect)

        py.draw.rect(screen, INPUT_BG_COLOR, self.output_rect)

        for i in range(len(self.output_text)):
            text_surface = self.font.render(self.output_text[i], True, UCA_BLUE)
            text_surface_rect = text_surface.get_rect()
            text_surface_rect.left = self.output_rect.left + 10
            text_surface_rect.top = self.output_rect.top + 10 + i * 40
            screen.blit(text_surface, text_surface_rect)
        
        # Go back button
        py.draw.rect(screen, BUTTON_COLOR, self.back_button)
        back_text = self.font.render("<-", True, TEXT_COLOR)
        back_text_rect = back_text.get_rect()
        back_text_rect.center = self.back_button.center
        screen.blit(back_text, back_text_rect)

        

    def handle_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            self.input_active = self.input_rect.collidepoint(event.pos)
        if event.type == py.KEYDOWN:
            if self.input_active:
                if event.key == py.K_RETURN and self.input_text.strip() != '':
                    if len(self.output_text) == 10:
                        self.output_text = self.output_text[1:]
                    self.output_text.append(self.input_text.strip() + " => " + self.get_hash_value(self.input_text.strip()))
                    self.input_text = ''
                elif event.key == py.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode
                self.input_text_surface = self.font.render(self.input_text, True, self.input_color)
        if event.type == py.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                return self.main_menu
        return self
    
    def get_hash_value(self, value):
        hash_value = 0
        prime = 31

        for char in value:
            hash_value = (hash_value * prime + ord(char)) % 101

        return str(hash_value)
         