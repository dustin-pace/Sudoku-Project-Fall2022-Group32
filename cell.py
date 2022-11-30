import pygame

CELL_WIDTH = 40
CELL_HEIGHT = CELL_WIDTH
LINE_WIDTH = 2
BLACK = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 32)

class Cell:
    """This class represents a single cell in the Sudoku board. There are 81 Cells in a Board."""

    def __init__(self, value, row, col, screen):
        """Constructor for the Cell class."""
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None

    def set_cell_value(self, value):
        """Setter for this cell’s value."""
        self.value = value

    def set_sketched_value(self, value):
        """Setter for this cell’s sketched value."""
        self.sketched_value = value

    def draw(self):
        """Draws this cell, along with the value inside it. If this cell has a nonzero value, that value is
        displayed. Otherwise, no value is displayed in the cell. The cell is outlined red if it is currently
        selected. """
        pygame.draw.rect(self.screen, BLACK, ((self.col, self.row), (CELL_WIDTH, CELL_HEIGHT)), width=LINE_WIDTH)

        display_value = font.render(f"{self.value}", True, BLACK)
        self.screen.blit(display_value, (self.col + CELL_WIDTH / 3, self.row + CELL_HEIGHT / 4))
