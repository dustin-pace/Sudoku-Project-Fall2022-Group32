import cell
import pygame
import sudoku_generator
from constants import *


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
        # Generate new Sudoku board
        sudoku_game = sudoku_generator.SudokuGenerator(BOARD_ROWS, self.difficulty)
        sudoku_solved = sudoku_generator.SudokuGenerator(BOARD_ROWS, self.difficulty)
        sudoku_game.fill_values()
        sudoku_solved.board = [item[:] for item in sudoku_game.board]
        sudoku_game.remove_cells()
        # Store game board and solved game board
        self.values = [item[:] for item in sudoku_game.board]
        self.solved = [item[:] for item in sudoku_solved.board]

        for i, b_row in enumerate(self.values):
            new_row = []
            for j, b_col in enumerate(b_row):
                new_row.append(cell.Cell(self.values[i][j], self.rows[i], self.columns[j], self.screen, i, j))
            self.board.append(new_row)
        """ Set the generated flag in the board"""
        for b_row in self.board:
            for b_col in b_row:
                if b_col.value == 0:
                    b_col.generated = False
                else:
                    b_col.generated = True


    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this
        board."""
        # self.screen.fill((WHITE))
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
        for board_row in self.board:
            for board_cell in board_row:
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
        for i, b_row in enumerate(self.board):
            for j, b_col in enumerate(b_row):
                if i == row and j == col:
                    if b_col.generated is False and b_col.selected is False:
                        b_col.selected = True
                        b_col.cell_color = RED
                        return True
                    elif b_col.generated is False and b_col.selected is True:
                        b_col.selected = False
                        b_col.cell_color = BLACK
                    elif b_col.generated:
                        return False
                    else:
                        b_col.selected = False
                        return False


    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row,
        col) of the cell which was clicked. Otherwise, this function returns None."""
        if x >= START and y >= START and x <= CELL_WIDTH * BOARD_COLS and y <= CELL_HEIGHT * BOARD_ROWS:
            col = x // CELL_WIDTH
            row = y // CELL_HEIGHT
            return row, col
        else:
            return None

    def clear(self):
        """Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves."""
        for row in self.board:
            for col in row:
                if col.generated == False and col.selected == True:
                    col.value = 0
                    col.sketched_value = 0

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value. It will be displayed in
        the top left corner of the cell using the draw() function."""
        for row in self.board:
            for col in row:
                if col.generated == False and col.selected == True:
                    col.sketched_value = value
                    # print(col.sketched_value)

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value. Called when the user presses the
        Enter key."""
        for row in self.board:
            for col in row:
                if col.generated == False and col.selected == True:
                    col.value = col.sketched_value
                    col.sketched_value = 0


    def reset_to_original(self):
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)."""
        for row in self.board:
            for col in row:
                if col.generated is False:
                    col.value = 0
                    col.sketched_value = 0
                    col.selected = False
                    col.cell_color = BLACK

    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        for row in self.board:
            for col in row:
                if col.value == 0:
                    return False
        return True

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                self.values[i][j] = col.value

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""
        for row in self.board:
            for col in self.board[row]:
                if self.board[row][col].value == 0 and self.board[row][col].sketched_value is None:
                    return row, col

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col.value != self.solved[i][j]:
                    # print(col.value, self.solved[i][j])
                    return False
        return True



