import pygame as py
from colors import *
from screens.hash_screen import HashScreen
from screens.tree_screen import TreeScreen
from screens.bst_screen import BinarySearchTreeScreen as BSTScreen

class MainMenu:
    def __init__(self, font) -> None:
        self.hash_button = py.Rect(100, 125, 400, 50)
        self.tree_button = py.Rect(100, 225, 400, 50)
        self.bst_button = py.Rect(100, 325, 400, 50)
        self.font = py.font.Font(font, 36)
        self.hash_screen = HashScreen(font)
        self.tree_screen = TreeScreen(font)
        self.bst_screen = BSTScreen(font)

    def draw(self, screen):
        screen.fill(WHITE)

        self.tree_button.center = screen.get_rect().center
        self.bst_button.center = screen.get_rect().center
        self.hash_button.center = screen.get_rect().center

        self.tree_button.y -= 100
        self.bst_button.y += 100

        py.draw.rect(screen, BUTTON_COLOR, self.hash_button)
        py.draw.rect(screen, BUTTON_COLOR, self.tree_button)
        py.draw.rect(screen, BUTTON_COLOR, self.bst_button)

        hash_text = self.font.render("Hash Dashboard", True, TEXT_COLOR)
        tree_text = self.font.render("Tree Dashboard", True, TEXT_COLOR)
        bst_text = self.font.render("Binary Search Tree Dashboard", True, TEXT_COLOR)

        hash_text_rect = hash_text.get_rect()
        tree_text_rect = tree_text.get_rect()
        bst_text_rect = bst_text.get_rect()

        hash_text_rect.center = self.hash_button.center
        tree_text_rect.center = self.tree_button.center
        bst_text_rect.center = self.bst_button.center

        screen.blit(hash_text, hash_text_rect)
        screen.blit(tree_text, tree_text_rect)
        screen.blit(bst_text, bst_text_rect)

    def handle_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            if self.hash_button.collidepoint(event.pos):
                return self.hash_screen
            elif self.tree_button.collidepoint(event.pos):
                return self.tree_screen
            elif self.bst_button.collidepoint(event.pos):
                return self.bst_screen
        