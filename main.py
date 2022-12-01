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
    w = 800
    h = 600

    #Colors:
    white = (255, 255, 255)
    light_green = (120, 179, 122)
    black = (0, 0, 0)

    #Fonts:
    start_title_border_font = pygame.font.Font(None, 101)
    start_title_font = pygame.font.Font(None, 100)
    game_mode_border_font = game_mode_font = pygame.font.Font(None, 76)
    game_mode_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    #Setting screen variable
    screen = pygame.display.set_mode((w,h))
    #Filling empty parts of screen with white color
    screen.fill((white))

    #Initialize title border
    title_border = start_title_border_font.render("Welcome to Sudoku", True, black)
    #Initialize title
    title = start_title_font.render("Welcome to Sudoku", True, white)

    #Initialize game mode title border
    game_mode_title_border = game_mode_border_font.render("Select Game Mode", True, black)
    #Initialize game mode title
    game_mode_title = game_mode_font.render("Select Game Mode", True, white)

    #Initialize buttons text:
    #Easy mode
    easy_mode_text = button_font.render("Easy", True, white)
    #Medium mode
    medium_mode_text = button_font.render("Medium", True, white)
    #Hard mode
    hard_mode_text = button_font.render("Hard", True, white)

    #Draw background image
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    #Draw title border
    screen.blit(title_border, [48, 49])
    #Draw title
    screen.blit(title, [50, 50])

    #Draw game mode border
    screen.blit(game_mode_title_border, [165, 274])
    #Draw game mode title
    screen.blit(game_mode_title, [170, 275])

    #Draw buttons:
    #Easy mode
    easy_mode = pygame.draw.rect(screen, light_green, pygame.Rect(125, 350, 150, 75))
    pygame.display.flip()
    #Medium mode
    medium_mode = pygame.draw.rect(screen, light_green, pygame.Rect(325, 350, 150, 75))
    pygame.display.flip()
    #Hard mode
    hard_mode = pygame.draw.rect(screen, light_green, pygame.Rect(525, 350, 150, 75))
    pygame.display.flip()

    #Draw button text:
    #Easy mode
    screen.blit(easy_mode_text, [160, 370])
    #Medium mode
    screen.blit(medium_mode_text, [335, 370])
    #Hard mode
    screen.blit(hard_mode_text, [560, 370])

    while(True):
        #Update the screen
        pygame.display.update()

        #If button is clicked
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_mode.collidepoint(event.pos):
                    #Print this to confirm that program works, need to change later
                    print("Easy")
                elif medium_mode.collidepoint(event.pos):
                    #Print this to confirm that program works, need to change later
                    print("Medium")
                elif hard_mode.collidepoint(event.pos):
                    #Print this to confirm that program works, need to change later
                    print("Hard")

def draw_game_over():
    #Activating Pygame library
    pygame.init()

    #Width/Height of image
    w = 800
    h = 600

    #Colors:
    white = (255, 255, 255)
    light_green = (120, 179, 122)
    black = (0, 0, 0)










#Call game_start screen
draw_game_start()




#Commenting this out for now, so I can test my code
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
