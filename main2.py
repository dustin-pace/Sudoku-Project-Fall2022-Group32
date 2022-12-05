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
    # screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
    #Filling empty parts of screen with white color
    # screen.fill((WHITE))

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
                    screen.fill((WHITE))
                    return 2
                elif medium_mode.collidepoint(event.pos):
                    screen.fill((WHITE))
                    return 40
                elif hard_mode.collidepoint(event.pos):
                    screen.fill((WHITE))
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
        screen.blit(restart_button_text, [225, 370])


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
                        return True
    return False

if __name__ == '__main__':
    #Activating PyGame library
    pygame.init()

    # Initialize game loop variables
    keep_playing = True

    # Main Loop for game
    while keep_playing:
        """ Initialize GUI loop variables """
        restart_game = False
        winner = False
        valid_selection = False
        input_val = 0
        game_over = False

        """ Draw game welcome, accept game difficulty setting"""
        screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
        mode = draw_game_start()

        """ Setup board in the board class for usage with GUI"""
        b = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, mode)
        screen.fill((WHITE))

        """ Setup and draw the buttons at the bottom of the screen """
        button_font = pygame.font.Font(None, BUTTON_FONT)

        """" Reset Button """
        gb_reset_button_text = button_font.render("Reset", True, WHITE)
        gb_reset_button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(RESET_BUTTON_START_H, GB_BUTTON_START_V, GB_BUTTON_WIDTH, GB_BUTTON_HEIGHT))
        pygame.display.flip()
        screen.blit(gb_reset_button_text, [RESET_BUTTON_START_H + 30, GB_BUTTON_START_V + 8])
        """Restart button"""
        gb_restart_button_text = button_font.render("Restart", True, WHITE)
        gb_restart_button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(RESTART_BUTTON_START_H, GB_BUTTON_START_V, GB_BUTTON_WIDTH, GB_BUTTON_HEIGHT))
        pygame.display.flip()
        screen.blit(gb_restart_button_text, [RESTART_BUTTON_START_H + 20, GB_BUTTON_START_V + 8])
        """Exit button"""
        gb_exit_button_text = button_font.render("Exit", True, WHITE)
        gb_exit_button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(EXIT_BUTTON_START_H, GB_BUTTON_START_V, GB_BUTTON_WIDTH, GB_BUTTON_HEIGHT))
        pygame.display.flip()
        screen.blit(gb_exit_button_text, [EXIT_BUTTON_START_H + 40, GB_BUTTON_START_V + 8])


        while not restart_game:
            b.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    keep_playing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if gb_reset_button.collidepoint(event.pos):
                        b.reset_to_original()
                        """These are for troubleshooting the Reset button
                        print('Reset Button pressed')
                        for i, row in enumerate(b.board):
                            for j, col in enumerate(row):
                                print(col.value, col.sketched_value, end=" ")
                            print()
                        print()
                        """
                    elif gb_restart_button.collidepoint(event.pos):
                        restart_game = True
                    elif gb_exit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                        keep_playing = False
                    selected_cell = b.click(event.pos[0], event.pos[1])
                    if selected_cell is not None:
                        valid_selection = b.select(selected_cell[0], selected_cell[1])
                    b.draw()
                elif event.type == pygame.KEYDOWN:  # Checks for key presses and if it's a number key
                    key_pressed = event.key
                    if event.key == pygame.K_1:
                        input_val = 1
                    elif event.key == pygame.K_2:
                        input_val = 2
                    elif event.key == pygame.K_3:
                        input_val = 3
                    elif event.key == pygame.K_4:
                        input_val = 4
                    elif event.key == pygame.K_5:
                        input_val = 5
                    elif event.key == pygame.K_6:
                        input_val = 6
                    elif event.key == pygame.K_7:
                        input_val = 7
                    elif event.key == pygame.K_8:
                        input_val = 8
                    elif event.key == pygame.K_9:
                        input_val = 9
                    elif event.key == pygame.K_RETURN:
                        if input_val != 0:
                            b.place_number(input_val)
                    else:
                        input_val = 0
                    b.sketch(input_val)  # sets the sketched value from user input
                    b.draw()

                    game_over = b.is_full() # Checks if the board is full, Boolean returned

                    if game_over:
                        winner = b.check_board()
                        restart_game = draw_game_over(winner)
            b.draw()
