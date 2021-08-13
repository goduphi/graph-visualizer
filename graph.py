from asset import Block
from color import Color


class Graph:
    def __init__(self, size, directed=False, cell_dimension=20):
        self.size = size
        self.cell_dimension = cell_dimension
        '''
            The matrix is filled with an array of Blocks which can be
            colored independently. The idea is to get a single block,
            color it accordingly, and then draw it to the screen
        '''
        self.grid = self.create_graph(size, cell_dimension)
        self.directed = directed

    def create_graph(self, size, cell_dimension):
        grid = []
        for row in range(size):
            grid.append([])
            for column in range(size):
                grid[row].append(Block(cell_dimension, cell_dimension, row, column, Color().white))
        return grid

    def reset(self):
        self.grid = self.create_graph(self.size, self.cell_dimension)

    def get_graph(self):
        return self.grid

    def add_edge(self, row, column):
        pass

    def get_block(self, coordinate):
        return self.grid[coordinate[0]][coordinate[1]]
