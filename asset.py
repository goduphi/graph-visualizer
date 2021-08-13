import pygame


class Block:
    def __init__(self, height, width, x, y, color=None):
        self.height = height
        self.width = width
        self.color = color
        self.edge = False
        self.selected = False
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color

    # Checks to see if this block has been selected by the user
    def is_selected(self):
        return self.selected

    # Signifies that the user selected the block using the mouse
    def select(self, selected):
        self.selected = selected

    def get_position(self):
        return self.x, self.y

    def get_dimension(self):
        return self.width, self.height

    # Draws the current block on to the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.y * self.width, self.x * self.height, self.width, self.height])
