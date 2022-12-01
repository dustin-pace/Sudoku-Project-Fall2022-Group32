import pygame

CELL_WIDTH = 40
CELL_HEIGHT = CELL_WIDTH
LINE_WIDTH = 2
BLACK = (0, 0, 0)
GREY = (126, 133, 128)
RED = (235, 64, 52)

# Initialize pygame fonts.
pygame.init()
font1 = pygame.font.Font(None, 32)          # Create font1 with a size of 32.
font2 = pygame.font.Font(None, 18)          # Create font2 with a size of 18.


class Cell:
    """This class represents a single cell in the Sudoku board. There are 81 Cells in a Board."""
    def __init__(self, value: int, row: int, col: int, screen: pygame.display) -> None:
        """Constructor for the Cell class."""
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.cell_color = BLACK
        self.selected = False
        self.generated = True
        self.position = []

    def set_cell_value(self, value: int) -> None:
        """Setter for this cell’s value."""
        self.value = value

    def set_sketched_value(self, value: int) -> None:
        """Setter for this cell’s sketched value."""
        self.sketched_value = value

    def set_pos(self, row, col):
        self.position.append(row)
        self.position.append(col)

    # TODO: Add highlighting functionality when cell is selected by user.
    def draw(self) -> None:
        """Draws this cell, along with the value inside it. If this cell has a nonzero value, that value is
        displayed. Otherwise, no value is displayed in the cell. The cell is outlined red if it is currently
        selected."""

        # Draw the cell outline.
        pygame.draw.rect(self.screen, self.cell_color, ((self.col, self.row), (CELL_WIDTH, CELL_HEIGHT)),
                         width=LINE_WIDTH)

        # Draw the cell value.
        display_value = font1.render(f"{self.value}", True, BLACK)
        self.screen.blit(display_value, (self.col + CELL_WIDTH / 3, self.row + CELL_HEIGHT / 4))

        # Check to see if user has created sketch value. If so, display value.
        if self.sketched_value is not None:
            sketch_value = font2.render(f"{self.sketched_value}", True, GREY)
            self.screen.blit(sketch_value, (self.col + CELL_WIDTH / 7, self.row + CELL_HEIGHT / 8))
