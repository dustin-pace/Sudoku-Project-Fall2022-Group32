import pygame
from constants import *


# Initialize pygame fonts.
pygame.init()
font1 = pygame.font.Font(None, BOARD_FONT1)          # Create font1 with a size of 32.
font2 = pygame.font.Font(None, BOARD_FONT2)          # Create font2 with a size of 18.


class Cell:
    """This class represents a single cell in the Sudoku board. There are 81 Cells in a Board."""
    def __init__(self, value: int, row: int, col: int, screen: pygame.display, r, c) -> None:
        """Constructor for the Cell class."""
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.cell_color = BLACK
        self.selected = False
        self.generated = True
        self.position = [r, c]

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
        pygame.draw.rect(self.screen, self.cell_color, pygame.Rect(self.col, self.row, CELL_WIDTH, CELL_HEIGHT), width=LINE_WIDTH_THIN)

        # Draw the cell value.
        if self.generated == True:
            display_value = font1.render(f"{self.value}", True, BLACK)
            self.screen.blit(display_value, (self.col + CELL_WIDTH / 3, self.row + CELL_HEIGHT / 3))
        else:
            if self.sketched_value == 0:
                if self.value == 0:
                    display_value = font1.render(f" ", True, WHITE)
                    self.screen.blit(display_value, (self.col + CELL_WIDTH / 6, self.row + CELL_HEIGHT / 6))
                else:
                    display_value = font1.render(f"{self.value}", True, BLACK)
                self.screen.blit(display_value, (self.col + CELL_WIDTH / 3, self.row + CELL_HEIGHT / 3))
            else:
                display_value = font2.render(f"{self.sketched_value}", True, GREY)
                self.screen.blit(display_value, (self.col + CELL_WIDTH / 6, self.row + CELL_HEIGHT / 6))
                if self.value != 0:
                    display_value = font1.render(f"{self.value}", True, BLACK)
                    self.screen.blit(display_value, (self.col + CELL_WIDTH / 3, self.row + CELL_HEIGHT / 3))

        # Check to see if user has created sketch value. If so, display value.
        # if self.sketched_value is not None:
        #     sketch_value = font2.render(f"{self.sketched_value}", True, GREY)
        #     self.screen.blit(sketch_value, (self.col + CELL_WIDTH / 7, self.row + CELL_HEIGHT / 8))
