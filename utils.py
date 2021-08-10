import pygame


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
