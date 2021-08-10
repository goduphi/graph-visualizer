class Block:
    def __init__(self, height, width, color=None):
        self.height = height
        self.width = width
        self.color = color
        self.edge = False

    def set_color(self, color):
        self.color = color

    def set_edge(self):
        self.edge = True

    def clear_edge(self):
        self.edge = False

    def is_edge(self):
        return self.edge
