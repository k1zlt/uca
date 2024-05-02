import pygame as py
from colors import *

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.x = 0
        self.y = 0

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class GraphScreen:
    def __init__(self, font, main_menu):
        self.nodes = {}
        self.font = py.font.Font(font, 36)
        self.back_button = py.Rect(50, 0, 100, 50)
        self.main_menu = main_menu

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            self.nodes[value1].add_neighbor(self.nodes[value2])
            self.nodes[value2].add_neighbor(self.nodes[value1])

    def handle_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            clicked_node = self.find_clicked_node(x, y)
            if clicked_node is None:
                value = len(self.nodes) + 1
                new_node = Node(value)
                new_node.x = x
                new_node.y = y
                self.nodes[value] = new_node
        if event.type == py.MOUSEBUTTONDOWN and self.back_button.collidepoint(event.pos):
            return self.main_menu

    def find_clicked_node(self, x, y):
        for node in self.nodes.values():
            if (node.x - x) ** 2 + (node.y - y) ** 2 <= 20 ** 2:
                return node
        return None

    def draw(self, screen):
        screen.fill(WHITE)
        py.draw.rect(screen, BUTTON_COLOR, self.back_button)
        back_text = self.font.render("<-", True, TEXT_COLOR)
        back_text_rect = back_text.get_rect()
        back_text_rect.center = self.back_button.center
        screen.blit(back_text, back_text_rect)

        for node in self.nodes.values():
            py.draw.circle(screen, UCA_BLUE, (node.x, node.y), 20)
            text_surface = self.font.render(str(node.value), True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(node.x, node.y))
            screen.blit(text_surface, text_rect)
            for neighbor in node.neighbors:
                py.draw.line(screen, UCA_BLUE, (node.x, node.y), (neighbor.x, neighbor.y), 2)
