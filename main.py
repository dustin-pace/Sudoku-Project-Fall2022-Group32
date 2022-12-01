#Import constants (Eventually?)
from constants import *
#Import the SudokuGenerator
from sudoku_generator import SudokuGenerator
#Import pygame for graphics
import pygame
#Import pygame locals, for image
from pygame.locals import*
#This will be te sudoku background image
background_image = pygame.image.load('Sudoku_Background_Image.jpg')

def draw_game_start():
    #Activating Pygame library
    pygame.init()

    #Width/Height of image
    w = 1000
    h = 1000

    #Setting screen variable
    screen = pygame.display.set_mode((w,h))
    #Setting color of screen
    white = (255, 255, 255)
    #Filling empty parts of screen with white color
    screen.fill((white))

    #Variable for whether or not game is ongoing
    game_ongoing = 1

    while(game_ongoing == 1):
        screen.blit(background_image, (0,0))
        pygame.display.flip()

draw_game_start()




#Commenting this out for now
'''
if __name__ == "__main__":
    """Main Program"""
    """Currently used for testing: MUST COMPLETE LATER"""
    sudoku_obj = SudokuGenerator(9,30)
    # for i, row in enumerate(sudoku_obj.board):
    #     for j, col in enumerate(row):
    #         print(sudoku_obj.board[i][j], end=" ")
    #     print()
    sudoku_obj.print_board()

    # print('Row Checks')
    # print(sudoku_obj.valid_in_row(0, 0))
    # print(sudoku_obj.valid_in_row(7, 10))
    # print('Column Checks')
    # print(sudoku_obj.valid_in_col(7, 2))
    # print(sudoku_obj.valid_in_col(2, 2))
    # print('Box Checks')
    # print(sudoku_obj.valid_in_box(0, 0, 0))
    # print(sudoku_obj.valid_in_box(0, 0, 2))
    # print(sudoku_obj.valid_in_box(0, 0, 3))
    # print('Check If Valid')
    # print(sudoku_obj.is_valid(0, 8, 9))
    # print(sudoku_obj.is_valid(3, 8, 9))

    # print('Filling Boxes')
    # sudoku_obj.fill_box(0, 0)
    # sudoku_obj.print_board()
    # sudoku_obj.fill_box(3, 3)
    # sudoku_obj.print_board()
    # sudoku_obj.fill_box(6, 6)
    # sudoku_obj.print_board()

    # print('Filling Diagonals')
    # sudoku_obj.fill_diagonal()
    # sudoku_obj.print_board()

    print('Filling Board')
    sudoku_obj.fill_values()
    sudoku_obj.print_board()
    print('\nRemoving Cells')
    sudoku_obj.remove_cells()
    sudoku_obj.print_board()

    print('\nNew Board')
    sudoku = SudokuGenerator(9, 60)
    sudoku.fill_values()
    sudoku.print_board()
    print()
    sudoku.remove_cells()
    sudoku.print_board()
'''
