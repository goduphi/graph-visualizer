'''
Grid code: http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
'''

import pygame
from color import Color
from asset import Block
from graph import Graph
from utils import *


def draw_grid(screen, grid, grid_size, block, color):
    pass


def main():
    # Variables to set dimensions
    window_size = (640, 640)
    color = Color()
    block = Block(20, 20, color.white)
    grid_size = window_size[0] // block.width - 3

    # Create a directed graph
    g = Graph(grid_size, True)

    pygame.init()
    screen = pygame.display.set_mode(window_size)

    done = False
    while not done:
        # Listen for user input here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                # Get the block which signifies the position in the matrix
                # where the user wants to put a break point
                # The // is integer division in python which I had no idea about
                column = mouse_position[0] // (block.width + 2)
                row = mouse_position[1] // (block.height + 2)

        screen.fill(color.black)

        for row in range(grid_size):
            for column in range(grid_size):
                # Get the current block
                block = g.get_block((row, column))
                block.set_color(color.white)
                draw_block(screen, block, row, column)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
