import cell
import pygame

CELL_WIDTH = 40
CELL_HEIGHT = CELL_WIDTH
LINE_WIDTH = 2
BLACK = (0, 0, 0)
GREY = (126, 133, 128)
RED = (235, 64, 52)

pygame.init()


class Board:
    """This class represents an entire Sudoku board. A Board object has 81 Cell objects."""

    def __init__(self, width: int, height: int, screen: pygame.display, difficulty: int) -> None:
        """Constructor for the Board class. Screen is a window from PyGame. Difficulty is a variable to indicate if
        the user chose easy, medium, or hard."""
        self.width = width
        self.height = height
        self.screen = screen
        self.difficult = difficulty
        self.columns = self.create_col_row(width)
        self.rows = self.create_col_row(height)

    @staticmethod
    def create_col_row(length) -> list:
        """If given the width or height of the board, returns a list of one-dimensional integers for the starting
        position of each column or row."""
        start = 35       # Offset from edge of board.
        end = length - start
        # For 9 col/rows, we need 8 equi-distant steps beyond starting point.
        step = round(((end - start) / 8), None)
        lengths = [start]
        for num in range(1, 9):
            lengths.append(start + step * num)
        return lengths

    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this
        board."""

        # Draw board outline.
        left = 70
        top = 70
        pygame.draw.rect(self.screen, BLACK, ((left, top), (self.width, self.height)), width=LINE_WIDTH)

        # TODO: Fix cell drawing. Working, but not perfect.
        #  Currently, cells are somewhat offset. May have to do with create_col_rows() staticmethod.

        # Draw individual cells.
        for row in self.rows:
            for col in self.columns:
                new_cell = cell.Cell(8, row+left/2, col+top/2, self.screen)
                new_cell.draw()


    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected,
        the user can edit its value or sketched value."""
        pass

    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row,
        col) of the cell which was clicked. Otherwise, this function returns None."""
        pass

    def clear(self):
        """Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves."""
        pass

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value. It will be displayed in
        the top left corner of the cell using the draw() function."""
        pass

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value. Called when the user presses the
        Enter key."""
        pass

    def reset_to_original(self):
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)."""
        pass

    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        pass

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        pass

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""
        pass

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""
        pass
