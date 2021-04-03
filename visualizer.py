'''
Grid code: http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
'''
import pygame
from color import Color
from asset import Block


# Utility functions
def draw_block(screen, block, y, x):
    margin = 2
    pygame.draw.rect(screen, block.color, [(block.width + margin) * x + margin,
                                           (block.height + margin) * y, block.width, block.height])


def init_grid(n):
    grid = []
    for row in range(n):
        grid.append([])
        for column in range(n):
            grid[row].append(0)
    return grid


def main():
    window_size = (640, 640)
    color = Color()
    block = Block(32, 32, color.white)
    grid_size = window_size[0] // block.width - 2
    grid = init_grid(grid_size)

    pygame.init()
    screen = pygame.display.set_mode(window_size)

    done = False
    while not done:
        # Listen to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                # Get the block which signifies the position in the matrix
                column = mouse_position[0] // (block.width + 2)
                row = mouse_position[1] // (block.height + 2)
                grid[row][column] = 1

        screen.fill(color.black)

        # Draw the grid
        for row in range(grid_size):
            for column in range(grid_size):
                block.set_color(color.white)
                if grid[row][column] == 1:
                    block.set_color(color.green)
                draw_block(screen, block, row, column)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
