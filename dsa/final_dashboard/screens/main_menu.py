import pygame as py
from colors import *
from screens.hash_screen import HashScreen
from screens.tree_screen import TreeScreen
from screens.bst_screen import BinarySearchTreeScreen as BSTScreen
from screens.graph_screen import GraphScreen

class MainMenu:
    def __init__(self, font) -> None:
        self.hash_button = py.Rect(100, 125, 200, 50)
        self.tree_button = py.Rect(100, 225, 200, 50)
        self.bst_button = py.Rect(100, 325, 200, 50)
        self.graph_button = py.Rect(100, 425, 200, 50)
        self.image = py.image.load('images/uca_logo.png')
        self.font = py.font.Font(font, 36)
        self.hash_screen = HashScreen(font, self)
        self.tree_screen = TreeScreen(font, self)
        self.bst_screen = BSTScreen(font, self)
        self.graph_screen = GraphScreen(font, self)

    def draw(self, screen):
        screen.fill(WHITE)
        py.draw.rect(screen, BUTTON_COLOR, self.hash_button)
        py.draw.rect(screen, BUTTON_COLOR, self.tree_button)
        py.draw.rect(screen, BUTTON_COLOR, self.bst_button)
        py.draw.rect(screen, BUTTON_COLOR, self.graph_button)

        hash_text = self.font.render("Hash", True, TEXT_COLOR)
        tree_text = self.font.render("Tree", True, TEXT_COLOR)
        bst_text = self.font.render("BST", True, TEXT_COLOR)
        graph_text = self.font.render("Graph", True, TEXT_COLOR)

        hash_text_rect = hash_text.get_rect()
        tree_text_rect = tree_text.get_rect()
        bst_text_rect = bst_text.get_rect()
        graph_text_rect = graph_text.get_rect()

        hash_text_rect.center = self.hash_button.center
        tree_text_rect.center = self.tree_button.center
        bst_text_rect.center = self.bst_button.center
        graph_text_rect.center = self.graph_button.center

        screen.blit(hash_text, hash_text_rect)
        screen.blit(tree_text, tree_text_rect)
        screen.blit(bst_text, bst_text_rect)
        screen.blit(graph_text, graph_text_rect)

        image_rect = self.image.get_rect()
        image_rect.center = screen.get_rect().center
        image_rect.x = 450
        screen.blit(self.image, image_rect)

    def handle_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            if self.hash_button.collidepoint(event.pos):
                return self.hash_screen
            elif self.tree_button.collidepoint(event.pos):
                return self.tree_screen
            elif self.bst_button.collidepoint(event.pos):
                return self.bst_screen
            elif self.graph_button.collidepoint(event.pos):
                return self.graph_screen
        