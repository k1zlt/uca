import pygame as py
from random import randint
from colors import *

root = None

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0
        self.height = 1

    def insert(self, root, value):
        if not root:
            root = Node(value)
            return root
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root  # Return the updated root after insertion


    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert_value(self, value):
        global root
        root = self.insert(root, value)
        return root

    def search(self, value: int) -> bool:
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        if self.right is None:
            return False
        return self.right.search(value)

    def print(self) -> None:
        if self.left:
            self.left.print()
        print(self.value,  end=" ")
        if self.right:
            self.right.print()


def assign_coordinates(node: Node, x: int, y: int, horizontal_space: int) -> None:
    if node is None:
        return
    if node.left:
        node.left.x = node.x - horizontal_space
        node.left.y = node.y + 60
        assign_coordinates(node.left, node.left.x, node.left.y, horizontal_space // 2)
    if node.right:
        node.right.x = node.x + horizontal_space
        node.right.y = node.y + 60
        assign_coordinates(node.right, node.right.x, node.right.y, horizontal_space // 2)



def generate_random_tree():
    global root
    root = Node(50)
    for _ in range(10):
        root.insert_value(randint(0, 100))
    return root

class BinarySearchTreeScreen():
    def __init__(self, font, main_menu) -> None:
        self.tree = generate_random_tree()
        self.tree.x = 400
        self.tree.y = 50
        self.font = py.font.Font(font, 36)
        self.main_menu = main_menu
        self.back_button = py.Rect(50, 0, 100, 50)
        assign_coordinates(self.tree, self.tree.x, self.tree.y, 200)

    def handle_event(self, event: py.event.Event) -> None:
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Reset button
                if 700 <= event.pos[0] <= 800 and 550 <= event.pos[1] <= 600:
                    self.tree.left = None
                    self.tree.right = None
                    assign_coordinates(self.tree, self.tree.x, self.tree.y, 200)
                # Add button
                if 700 <= event.pos[0] <= 800 and 500 <= event.pos[1] <= 550:
                    self.tree = self.tree.insert_value(randint(0, 100))
                    assign_coordinates(self.tree, self.tree.x, self.tree.y, 200)
                
                if self.back_button.collidepoint(event.pos):
                    return self.main_menu

    def draw_tree(self, screen, node):
        if node is not None:
            self.tree.x = 400
            self.tree.y = 50
            assign_coordinates(self.tree, self.tree.x, self.tree.y, 200)
            if node.left:
                py.draw.line(screen, UCA_BLUE, (node.x, node.y), (node.left.x, node.left.y), 2)
            if node.right:
                py.draw.line(screen, UCA_BLUE, (node.x, node.y), (node.right.x, node.right.y), 2)
            py.draw.circle(screen, UCA_BLUE, (node.x, node.y), 20) 
            text_surface = self.font.render(str(node.value), True, (255, 255, 255))
            screen.blit(text_surface, (node.x - 10, node.y - 10))
            self.draw_tree(screen, node.left)
            self.draw_tree(screen, node.right)

    def draw(self, screen) -> None:
        screen.fill(WHITE)
        reset_button = py.Rect(700, 550, 100, 50)
        py.draw.rect(screen, BUTTON_COLOR, reset_button)
        reset_text = self.font.render("Reset", True, TEXT_COLOR)
        reset_text_rect = reset_text.get_rect()
        reset_text_rect.center = reset_button.center
        screen.blit(reset_text, reset_text_rect)

        add_button = py.Rect(700, 500, 100, 50)
        py.draw.rect(screen, BUTTON_COLOR, add_button)
        add_text = self.font.render("Add", True, TEXT_COLOR)
        add_text_rect = add_text.get_rect()
        add_text_rect.center = add_button.center
        screen.blit(add_text, add_text_rect)

        py.draw.rect(screen, BUTTON_COLOR, self.back_button)
        back_text = self.font.render("<-", True, TEXT_COLOR)
        back_text_rect = back_text.get_rect()
        back_text_rect.center = self.back_button.center
        screen.blit(back_text, back_text_rect)


        self.draw_tree(screen, self.tree)