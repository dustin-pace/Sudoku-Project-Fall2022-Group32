import cell
import pygame
import sudoku_generator as sudoku

CELL_WIDTH = 40
CELL_HEIGHT = CELL_WIDTH
LINE_WIDTH = 2
BLACK = (0, 0, 0)
GREY = (126, 133, 128)
RED = (235, 64, 52)
START = 35  # Offset from edge of board.
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
        self.board = []
        self.values = sudoku.generate_sudoku(81, self.difficult)
        # 81 for debugging for now

    @staticmethod
    def create_col_row(length) -> list:
        """If given the width or height of the board, returns a list of one-dimensional integers for the starting
        position of each column or row."""

        end = length - START
        # For 9 col/rows, we need 8 equidistant steps beyond starting point.
        step = round(((end - START) / 8), None)
        lengths = [START]
        for num in range(1, 9):
            lengths.append(START + step * num)
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
                new_cell = cell.Cell(self.board[row][col], row + left / 2, col + top / 2, self.screen)
                new_cell.draw()
                new_cell.set_pos(row, col)
                if self.board[row][col] == 0:
                    new_cell.generated = False
                self.board[row][col] = new_cell

    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected,
        the user can edit its value or sketched value."""
        if self.board[row][col].generated == False and self.board[row][col].selected == False:
            self.board[row][col].selected = True
            return True
        elif self.board[row][col].generated:
            return False
        else:
            self.board[row][col].selected = False
            return False

    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row,
        col) of the cell which was clicked. Otherwise, this function returns None."""
        if START <= x <= CELL_WIDTH * 9 and START <= y <= CELL_HEIGHT * 9:
            row = x // CELL_WIDTH
            col = y // CELL_HEIGHT
            return row, col
        else:
            return None

    def clear(self):
        """Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].generated == False and self.board[row][col].selected == True:
                    self.board[row][col].value = 0
                    self.board[row][col].sketched_value = None

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value. It will be displayed in
        the top left corner of the cell using the draw() function."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].generated == False and self.board[row][col].selected == True:
                    self.board[row][col].sketched_value = value

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value. Called when the user presses the
        Enter key."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].generated == False and self.board[row][col].selected == True:
                    self.board[row][col].value = value

    def reset_to_original(self):
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)."""
        for row in self.board:
            for col in self.board[row]:
                if not self.board[row][col].generated:
                    self.board[row][col].value = 0
                    self.board[row][col].sketched_value = None

    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        for row in self.board:
            for col in self.board[row]:
                self.values[row][col] = self.board[row][col].value

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].value == 0 and self.board[row][col].sketched_value is None:
                    return row, col

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""
        pass



