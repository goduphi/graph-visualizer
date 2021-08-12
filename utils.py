import pygame


def init_grid(n):
    grid = []
    for row in range(n):
        grid.append([])
        for column in range(n):
            grid[row].append(0)
    return grid
