#################################################################
# FILE : game.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex9 2025
# DESCRIPTION: In this file I made the game class for the game rush-hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################

from board import Board

EXIT_COMMAND = "!"
CORRECT_DIRECTIONS = ["u", "d", "l", "r"]
UP_DIRECTION = "UP"
DOWN_DIRECTION = "DOWN"
RIGHT_DIRECTION = "RIGHT"
LEFT_DIRECTION = "LEFT"
STARTING_GAME = """Welcome,\nInstructions: Every name of car is named by one UPPER LETTER and every command is named by one lower letter, splitted by comma.\nFor example, If you want to move the car 'R' up, input is: R,u\nIf you want to exit the game press '!'\nLet's play Rush Hour!: """
INPUT_MSG_NAME_AND_DIRECTION = "Please insert name of car and direction: "
LENGTH_OF_INPUT_INVALID = "Length of the input is invalid, must be (name,direction)!"
NO_COMMA_IN_INPUT = "No comma (,) in input, must be (name, direction)!"
NAME_IS_NOT_CHARACHTER = "Name must be a charachter!"
DIRECTION_IS_NOT_CHARACHTER = "Direction must be a charachter!"
DIRECTION_INVALID = "Direction isn't valid, must be one of (u - up, d - down, l - left, r - right)"
NAME_GENERAL_ERROR = "Name not found in board *or* can't move this car!"
CAR_CANT_MOVE_BY_THIS_DIRECTION = "Incompatible direction to car, can't move this car in the direction given!"
GAME_STOPPED = "Game stopped by pressing '!', see you next time!"
WIN_MESSAGE = "Congratulations! You won the game."
POSSIBLE_MOVES_MESSAGE = "*All the possible moves can be done this turn*: "

class Game:
    """
    This class represents a game object of Rush-Hour game.
    Every game has:
    Board - a board object, which the user plays on
    """
    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board
        self.__game_ended = False

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        self.__print_possible_moves()
        name_and_direction = input(INPUT_MSG_NAME_AND_DIRECTION)
        if name_and_direction == EXIT_COMMAND:
            self.__game_ended = True
            return None # 'break'
        input_check = self.__check_validity_of_input(name_and_direction)
        if input_check != "":
            print(input_check)
            return None # 'break'
        name, direction = name_and_direction.split(",") # if got here, there is a comma so can be split
        # if got here, the turn can be done
        self.__board.move_car(name, direction)
        print(self.__board)

    def __print_possible_moves(self) -> None:
        """
        Prints all the possible moves in the turn
        """
        result = POSSIBLE_MOVES_MESSAGE
        possible_moves = self.__board.possible_moves()
        for move in possible_moves:
            car_name = move[0]
            direction = move[1]
            if direction == CORRECT_DIRECTIONS[0]:
                full_direction = UP_DIRECTION
            elif direction == CORRECT_DIRECTIONS[1]:
                full_direction = DOWN_DIRECTION
            elif direction == CORRECT_DIRECTIONS[2]:
                full_direction = LEFT_DIRECTION
            else: # direction == CORRECT_DIRECTIONS[3]:
                full_direction = RIGHT_DIRECTION
            description = move[2]
            result += f"\nThe car named {car_name} can move {direction} ({full_direction}) Because: {description}"
        print(result)

    def __check_validity_of_input(self, name_and_direction: str) -> str:
        """
        This function gets a string which needs to be name,direction in one string
        :param name_and_direction: string
        :return: "" if valid, else other error msg
        """
        if len(name_and_direction) != 3: # the format is (n,d) -> name, direction
            return LENGTH_OF_INPUT_INVALID
        if not "," in name_and_direction: # not valid input
            return NO_COMMA_IN_INPUT
        name, direction = name_and_direction.split(",") # if got here, can split by comma, because there is a comma
        if not name.isalpha(): # not an alphabethic charachter
            return NAME_IS_NOT_CHARACHTER
        if not direction.isalpha(): # not an alphabethic charachter
            return DIRECTION_IS_NOT_CHARACHTER
        if not direction in CORRECT_DIRECTIONS: # direction isn't one of udlr
            return DIRECTION_INVALID
        possible_moves = self.__board.possible_moves()
        moves_for_car = []
        for move in possible_moves: # every 'move' is a tuple of (name, move_key, description)
            if move[0] == name:
                moves_for_car.append(move)
        if not moves_for_car: # name not found in board \ can't move this car
            return NAME_GENERAL_ERROR
        direction_found = False
        for move in moves_for_car:
            if move[1] == direction:
                direction_found = True
        if not direction_found: # direction isn't valid for this car
            return CAR_CANT_MOVE_BY_THIS_DIRECTION
        return "" # if got here, the input is valid
        
    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        board = self.__board
        print(STARTING_GAME)
        print(board)
        # play until user press '!' or the target location isn't None (Win situation)
        while board.cell_content(board.target_location()) is None and self.__game_ended != True:
            self.__single_turn()
        if self.__game_ended: # user press '!'
            print(GAME_STOPPED)
        else:
            print(WIN_MESSAGE) # if got here, game stopped and user didn't press '!' so the user wins

