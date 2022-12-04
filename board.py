import cell
import pygame
import sudoku_generator as sudoku
from constants import *

# pygame.init()


class Board:
    """This class represents an entire Sudoku board. A Board object has 81 Cell objects."""

    def __init__(self, width: int, height: int, screen: pygame.display, difficulty: int) -> None:
        """Constructor for the Board class. Screen is a window from PyGame. Difficulty is a variable to indicate if
        the user chose easy, medium, or hard."""
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.screen = screen
        self.columns = self.create_col_row(CELL_WIDTH)
        self.rows = self.create_col_row(CELL_HEIGHT)
        self.board = []

        self.values = sudoku.generate_sudoku(BOARD_ROWS, self.difficulty)


        for i, row in enumerate(self.values):
            for j, col in enumerate(row):
                self.board.append(cell.Cell(self.values[i][j], self.rows[i], self.columns[j], self.screen, i, j))
        # Initialize generated field
        for cell1 in self.board:
            if cell1.value == 0:
                cell1.generated = False
            else:
                cell1.generated = True


    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this
        board."""
        self.screen.fill((WHITE))
        # Draw board outline.
        left = 0
        top = 0
        col_size = self.width // BOARD_COLS
        row_size = self.height // BOARD_ROWS
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(left, top, self.width, self.height), width=LINE_WIDTH_THICK)

        for i, row in enumerate(self.rows):
            for j, col in enumerate(self.columns):
                # pygame.draw.rect(self.screen, BLACK, pygame.Rect(row, col, CELL_WIDTH, CELL_HEIGHT), width=LINE_WIDTH_THIN)
                if i % 3 == 0 and j % 3 == 0:
                    pygame.draw.rect(self.screen, BLACK, pygame.Rect(row, col, CELL_WIDTH * 3, CELL_HEIGHT * 3), width=LINE_WIDTH_THICK)
        for i, board_cell in enumerate(self.board):
            board_cell.draw()



    @staticmethod
    def create_col_row(length) -> list:
        """If given the width or height of the board, returns a list of one-dimensional integers for the starting
        position of each column or row."""
        lengths = []
        # For 9 col/rows, we need 8 equidistant steps beyond starting point.
        for num in range(0, BOARD_COLS):
            lengths.append((START + length) * num)
        return lengths



    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected,
        the user can edit its value or sketched value."""
        for cell in self.board:
            if cell.position == [row, col]:
                if cell.generated is False and cell.selected is False:
                    cell.selected = True
                    cell.cell_color = RED
                    print(row, col, cell.position, cell.cell_color)
                    return True
                elif cell.generated:
                    return False
                else:
                    cell.selected = False
                    return False

    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row,
        col) of the cell which was clicked. Otherwise, this function returns None."""
        if x >= START and y >= START and x <= CELL_WIDTH * BOARD_COLS and y <= CELL_HEIGHT * BOARD_ROWS:
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



