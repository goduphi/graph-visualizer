'''
Author: Sarker Nadir Afridi Azmi
Grid code: http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
'''

import pygame
from color import Color
from graph import Graph
from utils import *
import math


def draw_grid(screen, g):
    screen.fill(Color().black)
    graph = g.get_graph()
    width = graph[0][0].get_dimension()[0]
    size = len(graph)
    n = 0
    for row in graph:
        for block in row:
            block.draw(screen)

    for row in range(size):
        pygame.draw.line(screen, Color().black, (0, row * width), (screen.get_height(), row * width))
        for column in range(size):
            pygame.draw.line(screen, Color().black, (column * width, 0), (column * width, screen.get_height()))

    pygame.display.flip()


def draw_shortest_distance(g, start, end, distance, draw):
    '''
        Look in all directions. Move towards the direction
        which will bring us closer to the start node.
    '''
    end_copy = end
    graph = g.get_graph()
    while end != start:
        x, y = end
        # Look up
        if distance[x - 1][y] < distance[x][y]:
            end = x - 1, y
        if distance[x + 1][y] < distance[x][y]:
            end = x + 1, y
        if distance[x][y + 1] < distance[x][y]:
            end = x, y + 1
        if distance[x][y - 1] < distance[x][y]:
            end = x, y - 1

        graph[end[0]][end[1]].set_color(Color().green)

        draw()

    x, y = start
    graph[x][y].set_color(Color().orange)
    x, y = end_copy
    graph[x][y].set_color(Color().blue)
    draw()


def bfs(g, start, end, draw):
    graph = g.get_graph()
    size = len(graph)
    color = Color().purple
    visited = [start]
    distance = [[math.inf for column in range(size)] for row in range(size)]

    # Set the distance of the source node to 0
    distance[start[0]][start[1]] = 0
    node_queue = [start]

    while len(node_queue) > 0:
        x, y = node_queue.pop(0)
        if (x, y) == end:
            draw_shortest_distance(g, start, end, distance, draw)
            return True
        '''
            We want to visit all the neighbors of the current node.
            Since it is a 2D matrix, we want to look to the right of the node,
            to the left of the node, the node above and the node below. If we
            have not visited that particular node, we visit it and add it to the
            queue to be processed later.
            
            Watch out for index out of bounds errors
        '''
        # Look to the right
        if y < size - 1 and not (graph[x][y + 1].get_position() in visited) and not graph[x][y + 1].is_barrier():
            node_queue.append(graph[x][y + 1].get_position())
            distance[x][y + 1] = distance[x][y] + 1
            graph[x][y + 1].set_color(color)
            visited.append(graph[x][y + 1].get_position())

        # Look below
        if x < size - 1 and not (graph[x + 1][y].get_position() in visited) and not graph[x + 1][y].is_barrier():
            node_queue.append(graph[x + 1][y].get_position())
            distance[x + 1][y] = distance[x][y] + 1
            graph[x + 1][y].set_color(color)
            visited.append(graph[x + 1][y].get_position())

        # Look to the left
        if x > 0 and not (graph[x - 1][y].get_position() in visited) and not graph[x - 1][y].is_barrier():
            node_queue.append(graph[x - 1][y].get_position())
            distance[x - 1][y] = distance[x][y] + 1
            graph[x - 1][y].set_color(color)
            visited.append(graph[x - 1][y].get_position())

        # Look above
        if y > 0 and not (graph[x][y - 1].get_position() in visited) and not graph[x][y - 1].is_barrier():
            node_queue.append(graph[x][y - 1].get_position())
            distance[x][y - 1] = distance[x][y] + 1
            graph[x][y - 1].set_color(color)
            visited.append(graph[x][y - 1].get_position())

        draw()

    return False


def main():
    # Variables to set dimensions
    window_size = (800, 800)
    color = Color()
    block_dimension = 20
    grid_size = window_size[0] // block_dimension

    # Create a directed graph
    g = Graph(grid_size, cell_dimension=block_dimension)
    start = None
    end = None

    pygame.init()
    pygame.display.set_caption("Graph Visualizer")
    screen = pygame.display.set_mode(window_size)

    done = False
    while not done:
        # Listen for user input here
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            (l, m, r) = pygame.mouse.get_pressed()

            # Get the block which signifies the position in the matrix
            # where the user wants to put a break point
            # The // is integer division in python which I had no idea about
            column = mouse_position[0] // block_dimension
            row = mouse_position[1] // block_dimension

            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                block = g.get_block((row, column))

                # There can can only be one start position
                # Left mouse button input
                if not r:
                    if l and not start:
                        # If the block position is the end position, don't select
                        if end == block.get_position():
                            break
                        start = (row, column)
                        block.set_color(Color().orange)
                    # Only let the user select one start position
                    elif l and start and start == block.get_position():
                        start = None
                        block.set_color(Color().white)

                # Right mouse button input
                if not l:
                    if r and not end:
                        # If the block position is the start position, don't select
                        if start == block.get_position():
                            break
                        end = (row, column)
                        block.set_color(Color().blue)
                    # Only let the user select one end position
                    elif r and end and end == block.get_position():
                        end = None
                        block.set_color(Color().white)

            if event.type == pygame.KEYDOWN:
                # Only run the algorithm if both the start and end conditions are defined
                # Use the Space key
                if event.key == pygame.K_SPACE and start and end:
                    bfs(g, start, end, lambda: draw_grid(screen, g))
                # Reset the visualizer using the R key
                if event.key == pygame.K_r:
                    g.reset()
                    start = end = None

                # Hover over block and press F to fill that block with a barrier
                if event.key == pygame.K_f:
                    block = g.get_block((row, column))
                    if block.get_position() != start and block.get_position() != end:
                        block.set_barrier(True)
                        block.set_color(Color().black)

        draw_grid(screen, g)

    pygame.quit()


if __name__ == "__main__":
    main()
