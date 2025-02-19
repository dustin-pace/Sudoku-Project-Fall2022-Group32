# Import the SudokuGenerator
from sudoku_generator import SudokuGenerator
# Import constants
from constants import *
# Import sys
import sys
# Import pygame for graphics
import pygame

# This will be the sudoku background image
background_image = pygame.image.load('Sudoku_Background_Image.jpg')


def draw_game_start():
    # Activating Pygame library
    pygame.init()

    # Fonts:
    start_title_border_font = pygame.font.Font(None, TB_FONT)
    start_title_font = pygame.font.Font(None, T_FONT)
    game_mode_border_font = pygame.font.Font(None, TB_FONT)
    game_mode_font = pygame.font.Font(None, T_FONT)
    button_font = pygame.font.Font(None, BUTTON_FONT)

    # Setting screen variable
    screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
    # Filling empty parts of screen with white color
    screen.fill((WHITE))

    # Initialize title
    title = start_title_font.render("Welcome to Sudoku", True, BLACK)

    # Initialize game mode title
    game_mode_title = game_mode_font.render("Select Game Mode", True, BLACK)

    # Initialize buttons text:
    # Easy mode
    easy_mode_text = button_font.render("Easy", True, WHITE)
    # Medium mode
    medium_mode_text = button_font.render("Medium", True, WHITE)
    # Hard mode
    hard_mode_text = button_font.render("Hard", True, WHITE)

    # Draw background image
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    # Draw title
    screen.blit(title, [TITLE_START_H, TITLE_START_V])

    # Draw game mode title
    screen.blit(game_mode_title, [GM_START_H, GM_START_V])

    # Draw buttons:
    # Easy mode
    easy_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(EM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()
    # Medium mode
    medium_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()
    # Hard mode
    hard_mode = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(HM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.display.flip()

    # Draw button text:
    # Easy mode
    screen.blit(easy_mode_text, [EM_START_H + 35, M_START_V + 15])
    # Medium mode
    screen.blit(medium_mode_text, [MM_START_H + 15, M_START_V + 15])
    # Hard mode
    screen.blit(hard_mode_text, [HM_START_H + 35, M_START_V + 15])

    while (True):
        # Update the screen
        pygame.display.update()

        # If button is clicked
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


# TODO: Fix function.
#  Function does not seem to behave properly with False argument.
#  Reset option is off-center.
def draw_game_over(won):
    # Activating Pygame library
    pygame.init()

    # Fonts:
    game_won_font = pygame.font.Font(None, T_FONT)
    game_lost_font = pygame.font.Font(None, T_FONT)
    button_font = pygame.font.Font(None, BUTTON_FONT)

    # Setting screen variable
    screen = pygame.display.set_mode((BG_WIDTH, BG_HEIGHT))
    # Filling empty parts of screen with white color
    screen.fill((WHITE))

    # Draw background image
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

    # Initialize game won
    game_won = game_won_font.render("You won!", True, BLACK)

    # Initialize game lost
    game_lost = game_lost_font.render("You lost!", True, BLACK)

    # Initialize exit button text
    exit_button_text = button_font.render("Exit", True, WHITE)
    # Initialize restart button text
    restart_button_text = button_font.render("Restart", True, WHITE)

    if won == True:
        # Draw text
        # screen.blit(game_won_border, [201, 151])
        screen.blit(game_won, [200, 150])
        # Draw exit button
        button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.display.flip()
        # Draw exit button text
        screen.blit(exit_button_text, [MM_START_H + 35, M_START_V + 15])
    elif won == False:
        # Draw text
        # screen.blit(game_lost_border, [201, 151])
        screen.blit(game_lost, [200, 150])
        # Draw restart button
        button = pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(MM_START_H, M_START_V, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.display.flip()
        # Draw restart button text
        screen.blit(restart_button_text, [340, 370])

    while True:
        # Update the screen
        pygame.display.update()

        # If button is clicked
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


# TODO: Build function.
def modify_cell():
    # Row = input from user
    row = int(input("Enter the row of the cell: ")) -1
    # Col = input from user
    col = int(input("Enter the column of the cell: ")) -1
    # Guess value = input from user
    num = int(input("Enter the value of the cell to enter: "))
    # Ask if this is a sketch value
    sketch = input("Is this a sketch value? Enter Y/N:")
    if sudoku_game.board[row][col] == 0:
        if sketch == "y" or sketch == "Y":
            sudoku_game.update_board_sketch(row, col, num)
            sudoku_game.print_board()
        elif sketch == "n" or sketch == "N":
            sudoku_game.update_board(row, col, num)
            sudoku_game.print_board()
        else:
            print("Please enter a correct option.\n Redoing cell input.")
            modify_cell()
    elif len(str(sudoku_game.board[row][col])) == 2:
        if sketch == "y" or sketch == "Y":
            sudoku_game.update_board_sketch(row, col, num)
            sudoku_game.print_board()
        elif sketch == "n" or sketch == "N":
            sudoku_game.update_board(row, col, num)
            sudoku_game.print_board()
        else:
            print("Please enter a correct option.\n Redoing cell input.")
            modify_cell()
    else:
        print("The selected cell cannot be edited.")
        sudoku_game.print_board()


def prompt_user() -> int:
    """Display CLI options to user. Ask user to make valid input. Returns user input."""
    try:
        user_input = int(input(OPTIONS1).strip())
        print()
        if user_input > 3 or user_input < 1:
            raise ValueError("Enter a valid integer")
    except ValueError as error:
        print(f"Error: {error}. Select a valid option.")
        print()
        prompt_user()

    # Return statement will only execute if valid assignment to user_input.
    return user_input


if __name__ == '__main__':
    # Activating PyGame library
    pygame.init()

    keep_playing = True
    # Main Loop for game
    while keep_playing:

        game_status = True

        """ Draw game welcome, accept game difficulty setting"""
        mode = draw_game_start()

        sudoku_game = SudokuGenerator(9, mode)
        sudoku_solved = SudokuGenerator(9, mode)
        sudoku_game.fill_values()
        sudoku_solved.board = [item[:] for item in sudoku_game.board]
        sudoku_game.remove_cells()

        # Print the board with zeros
        sudoku_game.print_board()

        # Newline
        print()

        # Demonstration of sketch functionality using solved_board.get_board() as optional argument.
        # sudoku_game.print_board(sudoku_solved.get_board())

        # Newline
        print()

        # Variable for whether player won the game or not
        won = 0

        while (game_status == True):
            user_prompt = prompt_user()
            # If the user types 1, type which cell to guess, then
            if user_prompt == 1:
                modify_cell()

            # If the user types 2, reset the sudoku game
            elif user_prompt == 2:
                for i in range(0, 9):
                    for j in range(0, 9):
                        cell = str(sudoku_game.board[i][j])
                        for c in cell:
                            if c == '*':
                                # Update the sudoku board list
                                sudoku_game.update_board_reset(i, j, 0)
                print("The board has been reset.")
                sudoku_game.print_board()


            elif user_prompt == 3:
                # Just need to break out of game_status == True loop
                # Doesn't work yet
                print("Restarting game.")
                break


            elif user_prompt == 4:
                print("Thank you for playing!")
                quit()

            if sudoku_game.board == sudoku_solved.board:
                print("Congratulations. You solved the Sudoku board!")
                again = input("Do you want to keep playing? Enter Y/N.")
                if again == "Y" or again == "y":
                    print("Restarting game.")
                    game_status == False
                    continue
                elif again == "N" or again == "n":
                    print("Thank you for playing!")
                    quit()
        continue
    draw_game_over(won)
