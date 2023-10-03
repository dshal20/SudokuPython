import pygame # A built-in game generator in python

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.width = 89 # Width of the cell on the screen
        self.height = 89 # Height of the cell on the screen
        self.selected = False


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x_plane = self.col * self.width
        y_plane = self.row * self.height
        font = pygame.font.Font(None, 40) # Creates Pygame font

        if self.selected: # Draws a red outline around the cell if selected
            pygame.draw.rect(self.screen, (255, 0, 0), (x_plane, y_plane, self.width, self.height), 3)

        if self.value != 0: # Displays value in the cell if not zero
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x_plane + self.width / 2, y_plane + self.height / 2))
            self.screen.blit(text, text_rect)

        elif self.sketched_value is not None: # If the cell has a sketched value it display value in gray
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text.get_rect(center=(x_plane + self.width / 6.5, y_plane + self.height / 5.5))
            self.screen.blit(text, text_rect)