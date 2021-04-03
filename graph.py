class Graph:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for column in range(size)] for row in range(size)]

    def add_edge(self, row, column, directed=True):
        if row < 0 or row > self.size or column < 0 or column > self.size:
            return False
        self.grid[row][column] = 1
        if not directed:
            self.grid[column][row] = 1