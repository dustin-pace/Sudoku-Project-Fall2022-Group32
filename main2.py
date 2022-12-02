#Import constants (Eventually?)
from constants import *
#Import the SudokuGenerator
from sudoku_generator import SudokuGenerator
#Import pygame for graphics
import pygame
#Import sys
import sys
from board import *

if __name__ == "__main__":
    """Main Program"""
    """Currently used for testing: MUST COMPLETE LATER"""
    difficulty = 'easy'
    if difficulty == 'easy':
        mode = 30
    elif difficulty == 'medium':
        mode = 40
    elif diffuculty == 'hard':
        mode = 50
    else:
        print('Invalid difficulty selection: please enter easy, medium, or hard')

    sudoku_game = SudokuGenerator(9, mode)
    sudoku_solved = SudokuGenerator(9, mode)
    sudoku_game.fill_values()
    sudoku_solved.board = [item[:] for item in sudoku_game.board]
    sudoku_game.remove_cells()
    sudoku_solved.print_board()
    print()
    sudoku_game.print_board()
