#################################################################
# FILE : lab4.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs lab4 2025
# DESCRIPTION: In this file I created a nims game
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: How to print in colors - https://shorturl.at/a1lyB
# NOTES: None
#################################################################

# This is const of number of rows and nims sign for the terminal
NUMBER_OF_ROWS = 4
NIM = "|"
# This is messages that the user will see as output on the screen only when he needs to
ROW_INPUT_MSG = "Please enter number of row: "
NIM_INPUT_MSG = "Please enter number of nims to take"
ROW_INPUT_ERROR_MSG = "Number of row is not valid!"
NIM_INPUT_ERROR_MSG = "Number of nims is not valid!"
# This is colors to the terminal
PLAYER_1_COLOR = "\033[7;31m"
PLAYER_2_COLOR = "\033[7;34m"
WIN_COLOR = "\033[92m"
RESET_COLOR = "\033[0m"

def init_board():
    """
    This function initializing a board, that is a list
    The length of the list(board) is the number of rows and each cell has the number of nims in it
    """
    board = []
    num_of_nims = 1
    for i in range(NUMBER_OF_ROWS):
        board.append(i + num_of_nims)
        num_of_nims += 1
    return board

def print_board(board):
    """
    This function gets a board and print it
    """
    for i in range(len(board)):
        print(f"Row {i+1}", end = "\t")
        for j in range(board[i]):
            print(NIM, end = "  ")
        print()

def get_input(msg):
    """
    This function gets a message and request an input from the user
    """
    return input(msg)

def is_board_empty(board):
    """
    This function checks if a board is empty
    """
    for i in range(len(board)):
        if board[i] > 0:
            return False
    return True

def check_row_number_validity(board, row_num):
    """
    This function checks if the row_num is a valid row number in the board
    """
    if not row_num.isnumeric(): # If its not a number
        return False
    row_num = int(row_num)
    if row_num > len(board) or row_num < 1: # If the number is not valid
        return False
    return True

def check_ammount_taken(board, row_num, num_of_nims): 
    """
    This function checks if the num_of_nims is a valid ammount of nims to take from row_num
    """
    if not num_of_nims.isnumeric(): # If its not a number
        return False
    num_of_nims = int(num_of_nims)
    if num_of_nims < 0 or num_of_nims > board[int(row_num)-1]: # If the number is not valid
        return False
    return True

def get_next_player(curr_player):
    """
    This function get a player and return the next player
    """
    if curr_player == "Player #1":
        return "Player #2"
    else:
        return "Player #1"

def show_msg(MSG):
    """
    This function gets a message and prints it to the user
    """
    print(MSG)

def update_board(board, row_num, nim_num):
    """
    This function gets a board and update it
    """
    board[int(row_num)-1] -= int(nim_num)

def print_who_plays(curr_player):
    """
    This function prints who plays right now - whose turn is it
    """
    if curr_player == "Player #1":
        show_msg(f"{PLAYER_1_COLOR}{curr_player} Turn! {RESET_COLOR}")
    else:
        show_msg(f"{PLAYER_2_COLOR}{curr_player} Turn! {RESET_COLOR}")

def run_game():
    """
    This function runs the nim game
    """
    board = init_board() # initializing a board
    curr_player = "Player #1" # player 1 starts as default
    while not is_board_empty(board): # run until the board is empty and there is a winner
        print_board(board) # print the board
        print_who_plays(curr_player) 
        row_num = get_input(ROW_INPUT_MSG)
        while not check_row_number_validity(board, row_num): # run until the input is valid
            show_msg(ROW_INPUT_ERROR_MSG)
            row_num = get_input(ROW_INPUT_MSG)
        nim_num = get_input(f"{NIM_INPUT_MSG} From Row {int(row_num)}: ")
        while not check_ammount_taken(board, row_num, nim_num): # run until the input is valid
            show_msg(NIM_INPUT_ERROR_MSG)
            nim_num = get_input(f"{NIM_INPUT_MSG} From Row {int(row_num)}: ")
        update_board(board, row_num, nim_num) # update the board with the valid row number and number of nims to take
        if is_board_empty(board): # if there is a winner at this turn
            show_msg(f"{WIN_COLOR}{curr_player} Wins! {RESET_COLOR}")
            break
        curr_player = get_next_player(curr_player)

def main():
    run_game()

if __name__ == '__main__':
    main()