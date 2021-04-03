class Block:
    def __init__(self, height, width, color=None):
        self.height = height
        self.width = width
        self.color = color

    def set_color(self, color):
        self.color = color