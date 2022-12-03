#Import constants (Eventually?)
from constants import *
#Import the SudokuGenerator
from sudoku_generator import SudokuGenerator
#Import the Board class
from board import Board
#Import the cell class
from cell import Cell
#Import constants
from constants import *
#Import sys
import sys
#Import pygame for graphics
import pygame

#This will be te sudoku background image
background_image = pygame.image.load('Sudoku_Background_Image.jpg')

def draw_game_start():
    #Activating Pygame library
    pygame.init()

    #Fonts:
    start_title_border_font = pygame.font.Font(None, TB_FONT)
    start_title_font = pygame.font.Font(None, T_FONT)
    game_mode_border_font = pygame.font.Font(None, TB_FONT)
    game_mode_font = pygame.font.Font(None, T_FONT)
    button_font = pygame.font.Font(None, BUTTON_FONT)

    #Setting screen variable
    screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
    #Filling empty parts of screen with white color
    screen.fill((WHITE))

    #Initialize title
    title = start_title_font.render("Welcome to Sudoku", True, BLACK)

    #Initialize game mode title
    game_mode_title = game_mode_font.render("Select Game Mode", True, BLACK)

    #Initialize buttons text:
    #Easy mode
    easy_mode_text = button_font.render("Easy", True, WHITE)
    #Medium mode
    medium_mode_text = button_font.render("Medium", True, WHITE)
    #Hard mode
    hard_mode_text = button_font.render("Hard", True, WHITE)

    #Draw background image
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    #Draw title
    screen.blit(title, [TITLE_START_H, TITLE_START_V])

    #Draw game mode title
    screen.blit(game_mode_title, [GM_START_H, GM_START_V])

    #Draw buttons:
    #Easy mode
    easy_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(EM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()
    #Medium mode
    medium_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()
    #Hard mode
    hard_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(HM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()

    # Draw button text:
    # Easy mode
    screen.blit(easy_mode_text, [EM_START_H + 35, M_START_V + 15])
    # Medium mode
    screen.blit(medium_mode_text, [MM_START_H + 15, M_START_V + 15])
    # Hard mode
    screen.blit(hard_mode_text, [HM_START_H + 35, M_START_V + 15])

    while(True):
        # Update the screen
        pygame.display.update()

        #If button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_mode.collidepoint(event.pos):
                    # Print this to confirm that program works, need to change later
                    print("Easy")
                    # Returns to main
                    # pygame.quit()
                    screen.fill((WHITE))
                    return 30
                elif medium_mode.collidepoint(event.pos):
                    # Print this to confirm that program works, need to change later
                    print("Medium")
                    # Returns to main
                    pygame.quit()
                    return 40
                elif hard_mode.collidepoint(event.pos):
                    # Print this to confirm that program works, need to change later
                    print("Hard")
                    # Returns to main
                    pygame.quit()
                    return 50

def draw_game_over(won):
    #Activating Pygame library
    pygame.init()

    #Fonts:
    game_won_font = pygame.font.Font(None, T_FONT)
    game_lost_font = pygame.font.Font(None, T_FONT)
    button_font = pygame.font.Font(None, BUTTON_FONT)

    #Setting screen variable
    screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
    #Filling empty parts of screen with white color
    screen.fill((WHITE))

    #Draw background image
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    # Initialize game won
    game_won = game_won_font.render("You won!", True, BLACK)

    #Initialize game lost
    game_lost = game_lost_font.render("You lost!", True, BLACK)

    #Initialize exit button text
    exit_button_text = button_font.render("Exit", True, WHITE)
    #Initialize restart button text
    restart_button_text = button_font.render("Restart", True, WHITE)

    if won == True:
        #Draw text
        # screen.blit(game_won_border, [201, 151])
        screen.blit(game_won, [200, 150])
        #Draw exit button
        button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.display.flip()
        #Draw exit button text
        screen.blit(exit_button_text, [MM_START_H + 35, M_START_V + 15])
    elif won == False:
        #Draw text
        # screen.blit(game_lost_border, [201, 151])
        screen.blit(game_lost, [200, 150])
        #Draw restart button
        button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.display.flip()
        #Draw restart button text
        screen.blit(restart_button_text, [340, 370])


    while (True):
        #Update the screen
        pygame.display.update()

        #If button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    if won == True:
                        pygame.quit()
                        sys.exit()
                    elif won == False:
                        print("Restarted")



if __name__ == '__main__':
    #Activating PyGame library
    pygame.init()

    keep_playing = True
    # Main Loop for game
    while keep_playing:
        """ Draw game welcome, accept game difficulty setting"""
        mode = draw_game_start()

        """ Setup board in the board class for usage with GUI"""
        b = Board(BOARD_WIDTH, BOARD_HEIGHT, pygame.display.set_mode((BG_WIDTH, BG_HEIGHT)), mode)

        """ Used for console version
        sudoku_game = SudokuGenerator(9, mode)
        sudoku_solved = SudokuGenerator(9, mode)
        sudoku_game.fill_values()
        sudoku_solved.board = [item[:] for item in sudoku_game.board]
        sudoku_game.remove_cells()
        """

        """ Used this section for testing that the boards were configured correctly
        sudoku_solved.print_board()
        print()
        sudoku_game.print_board()
        print()
        b.board = sudoku_game.board
                
        for i, row in enumerate(b.board):
            for j, col in enumerate(row):
                print(b.board[i][j], end=" ")
            print()
            
        """


        while (True):
            b.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_cell = b.click(event.pos[0], event.pos[1])
                print(selected_cell)
                valid_selection = b.select(selected_cell[0], selected_cell[1])
                print(valid_selection)






        keep_playing = False
        draw_game_over(True)
