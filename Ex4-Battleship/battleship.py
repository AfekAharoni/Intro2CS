#################################################################
# FILE : battleship.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex4 2025
# DESCRIPTION: In this file I created a battleships game
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: How to copy a list with a shallow copy without import copy - https://tinyurl.com/yf7yhh79
# NOTES: None
#################################################################
import helper

# This is messages that the user will see as output on the screen only when he needs to
INPUT_MSG_FOR_SHIP_PLACEMENT = "Enter a valid top location for ship of size"
ERORR_MSG_NOT_IN_FORMAT = "Cell name isn't correct! The format for cell name is XN, X is a char and N is a number."
ERROR_MSG_CANT_PLACE_A_SHIP = "Location not valid! Can't place a ship here."
INPUT_MSG_FOR_TORPEDO_LOCATION = "Enter torpedo target location: "
ERROR_MSG_FOR_TORPEDO_LOCATION = "Can't place a torpedo here, try again"
PLAYER_WINS_MSG = "Player Wins!"
COMPUTER_WINS_MSG = "Computer Wins!"
TIED_MSG = "Tied!"
PLAY_AGAIN_MSG = "Want to play again? "
ERROR_MSG_FOR_PLAY_AGAIN = "Invalid Answer. Y for yes, N for no."

def init_board(rows, columns):
    """
    This function gets rows and columns, and creates a board of in size of columns*rows
    The function returns the board created
    """
    board_line = []
    board = []
    for i in range(rows):
        for j in range(columns):
            board_line.append(helper.WATER)
        board.append(board_line)
        board_line = []
    return board

def valid_ship(board, size, loc):
    """ 
    This function gets a board, size of a ship and a location
    The function returns True if a ship can be placed in the location with its size, and False else
    """
    row = loc[0] # The row part of the tuple
    column = loc[1] # The column part of the tuple
    if column > len(board[0]) or row >= len(board): # If the location isn't valid
        return False
    if size > len(board) - row or size < 0: # If the size of the ship is bigger than the size from the location
        return False
    for i in range(row, row+size):
        if board[i][column] != helper.WATER: # If this location isn't water
            return False
    return True

def cell_name_to_loc(name):
    """
    This function gets name in format XN: X - number of column which represent in char, N - number of row
    The function assumes that 'name' is in correct format
    """
    column = ord(name[0]) - 65
    row = int(name[1:]) - 1
    return row, column

def set_ship(board, ship_size, col_row_tup):
    """
    This function gets a board, ship size and a location and place a ship in this location
    The ship size represent the head of the ship
    """
    row = col_row_tup[0]
    column = col_row_tup[1]
    for i in range(row, row + ship_size):
        board[i][column] = helper.SHIP # Set a ship in this location
    return board

def create_player_board(rows, columns, ship_sizes):
    """
    This function creates player board by rows, columns and tuple of ship_sizes got as arguments
    """
    board = init_board(rows, columns) # Initializing a board by sizes got 
    index_of_ship = 0 
    while index_of_ship < len(ship_sizes): # Run only if there is no ships that had placed
        helper.show_board(board)
        cell_name = (helper.get_input(f"{INPUT_MSG_FOR_SHIP_PLACEMENT} {ship_sizes[index_of_ship]}: ")).upper()
        while not helper.is_cell_name(cell_name) or int(cell_name[1:]) <= 0: # Run until the input is correct
            helper.show_msg(f"{ERORR_MSG_NOT_IN_FORMAT}")
            helper.show_board(board)
            cell_name = (helper.get_input(f"{INPUT_MSG_FOR_SHIP_PLACEMENT} {ship_sizes[index_of_ship]}: ")).upper()
        loc = cell_name_to_loc(cell_name) # If the function gets here, the cell_name format is correct
        if valid_ship(board, ship_sizes[index_of_ship], loc): # If the ship can be placed here, it will be
            board = set_ship(board, ship_sizes[index_of_ship], loc)
            index_of_ship += 1 # Next ship, if there is another one
        else: # Can't place a ship here, informative message to the user
            helper.show_msg(f"{ERROR_MSG_CANT_PLACE_A_SHIP}")
    return board

def valid_location_placements(board, size):
    """
    This function gets a board and a size of ship, and return all the locations that the ship can be placed in as a set
    """
    set_of_locations = set() # Initializing a set
    for i in range(len(board)):
        for j in range(len(board[0])):
            loc = (i, j) # Tuple of row, column
            if valid_ship(board, size, loc):
                set_of_locations.add(loc)
    return set_of_locations
    
def create_computer_board(rows, columns, ship_sizes):
    """
    This function creates computer board by rows, columns, and ship_sizes got as arguments
    """
    board = init_board(rows, columns) # Initializing the board
    valid_location_placement = None
    for ship_size in ship_sizes:
        valid_location_placement = valid_location_placements(board, ship_size) # Get a set of all locations a ship can be placed in
        loc = helper.choose_ship_location(board, ship_size, valid_location_placement) # Choose randomally where to place the ship
        board = set_ship(board, ship_size, loc)
    return board

def is_hidden_ships(computer_board, player_board):
    """
    This function checks if there are ships that are still hidden (not damaged ships)
    """
    computer_board_has_hidden_ships = False
    player_board_has_hidden_ships = False
    for row in range(len(computer_board)):
        for column in range(len(computer_board[0])):
            if computer_board[row][column] == helper.SHIP: # If there is one index with ship, the game didn't end
                computer_board_has_hidden_ships = True
            if player_board[row][column] == helper.SHIP: # If there is one index with ship, the game didn't end
                player_board_has_hidden_ships = True
    return player_board_has_hidden_ships and computer_board_has_hidden_ships # If both boards still has hidden ships, the game will continue

def hide_ships(board):
    """
    This function gets a board and hide the ships there
    """
    hidden_board = [row[:] for row in board] # Shallow copy the board content
    for row in range(len(hidden_board)):
        for column in range(len(hidden_board[0])):
            if hidden_board[row][column] == helper.SHIP: # Hide the ship to water
                hidden_board[row][column] = helper.WATER
    return hidden_board

def valid_torpedo_location(board, cell_name):
    """
    This function gets board and cell_name and returns if the location is a valid torpedo location
    """
    if not helper.is_cell_name(cell_name): # If this is not valid location
        return False
    if int(cell_name[1:]) <= 0: # Not valid location too
        return False
    location = cell_name_to_loc(cell_name)
    if location[0] >= len(board) or location[1] >= len(board[0]): # Out of range of the board
        return False
    if board[location[0]][location[1]] == helper.HIT_SHIP or board[location[0]][location[1]] == helper.HIT_WATER: # This index already damaged and not hidden
        return False
    return True

def options_to_torpedo(board):
    """
    This function gets a board and returns set of all the options a torpedo can be shot to (not already damaged indexes)
    """
    set_of_locations = set() # Initializing a set
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == helper.WATER or board[i][j] == helper.SHIP: # If the index hadn't got a torpedo yet
                set_of_locations.add((i, j))
    return set_of_locations

def shoot_torpedo(board, location):
    """
    This function gets a board and location, and hit a torpedo to the location
    """
    new_board = board
    if new_board[location[0]][location[1]] == helper.WATER: # If it's water, change to hit_water
        new_board[location[0]][location[1]] = helper.HIT_WATER
    elif new_board[location[0]][location[1]] == helper.SHIP: # If it's ship, change to hit_ship
        new_board[location[0]][location[1]] = helper.HIT_SHIP
    return new_board

def is_fleet_destroyed(board):
    """
    This function gets a board and checks if the fleet destroyed or not
    """
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == helper.SHIP: # If there is a ship, the fleet isn't destroyed
                return False
    return True

def check_valid_answer(answer):
    """
    This function checks if the answer of the user is correct or not
    """
    if answer != "Y" and answer != "N":
        return False
    return True

def check_for_winners(player_board, computer_board):
    """
    This function gets 2 boards, and checks if one of them already wins
    If player_board is destroyed, computer wins, if computer_board is destroyed - player wins, if both destroed = It's a tie
    """
    helper.show_board(player_board, computer_board) # Print the two boards
    if is_fleet_destroyed(computer_board) and not is_fleet_destroyed(player_board): # If player is the winner
        helper.show_msg(f"{PLAYER_WINS_MSG}")
    elif is_fleet_destroyed(player_board) and not is_fleet_destroyed(computer_board): # If computer is the winner
        helper.show_msg(f"{COMPUTER_WINS_MSG}")
    else: # If both of them are winners
        helper.show_msg(f"{TIED_MSG}")

def main():
    computer_board = create_computer_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES) # Initalizing computer board
    player_board = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES) # Initializing player board
    torpedo_options_for_computer = None
    want_to_play = True
    answer_of_wanna_play = None
    while want_to_play: # Run only if the player wants to play, minimum one run
        while is_hidden_ships(computer_board, player_board): # Run only if there are still hidden ships (the game didn't end)
            helper.show_board(player_board, hide_ships(computer_board)) # Print the two boards
            player_torpedo_cell_name = (helper.get_input(f"{INPUT_MSG_FOR_TORPEDO_LOCATION}")).upper() # Asks to get a torpedo location from the player
            while not valid_torpedo_location(computer_board, player_torpedo_cell_name): # Runs until the location is correct
                helper.show_msg(f"{ERROR_MSG_FOR_TORPEDO_LOCATION}")
                helper.show_board(player_board, hide_ships(computer_board)) # Print the two boards
                player_torpedo_cell_name = (helper.get_input(f"{INPUT_MSG_FOR_TORPEDO_LOCATION}")).upper()
            player_torpedo_location = cell_name_to_loc(player_torpedo_cell_name)
            torpedo_options_for_computer = options_to_torpedo(player_board) # Get a set of locations that can be attacked for computer
            torpedo_target_for_computer = helper.choose_torpedo_target(player_board, torpedo_options_for_computer) # Choose one from the set
            player_board = shoot_torpedo(player_board, torpedo_target_for_computer) # Player shoot torpedo to computer
            computer_board = shoot_torpedo(computer_board, player_torpedo_location) # Computer shoot torpedo to player
            if is_fleet_destroyed(computer_board) or is_fleet_destroyed(player_board): # If at least one of them destroyed, the game end
                check_for_winners(player_board, computer_board)
                answer_of_wanna_play = helper.get_input(f"{PLAY_AGAIN_MSG}") # Ask for user to play again
                while not check_valid_answer(answer_of_wanna_play): # Run until the answer is correct
                    helper.show_msg(f"{ERROR_MSG_FOR_PLAY_AGAIN}")
                    answer_of_wanna_play = helper.get_input(f"{PLAY_AGAIN_MSG}")
                if answer_of_wanna_play == "N": # If the player don't want to play again
                    want_to_play = False # Quit the while (break)
                else: # The player wants to play another game, so initializing the two boards again
                    computer_board = create_computer_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)
                    player_board = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)

if __name__ == "__main__":
    main()
