from asset import Block
from color import Color


class Graph:
    def __init__(self, size, directed=False, cell_dimension=20):
        self.size = size
        '''
            The matrix is filled with an array of Blocks which can be
            colored independently. The idea is to get a single block,
            color it accordingly, and then draw it to the screen
        '''
        self.grid = [[Block(cell_dimension, cell_dimension, Color().white) for column in range(size)] for row in range(size)]
        self.directed = directed

    def get_graph(self):
        return self.grid

    def add_edge(self, row, column):
        if row < 0 or row > self.size or column < 0 or column > self.size:
            return False
        self.grid[row][column].set_edge()
        if not self.directed:
            self.grid[column][row].set_edge()

    def get_block(self, coordinate):
        return self.grid[coordinate[0]][coordinate[1]]
