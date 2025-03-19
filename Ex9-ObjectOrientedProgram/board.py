#################################################################
# FILE : board.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex9 2025
# DESCRIPTION: In this file I made the board class for the game rush-hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################

from typing import Tuple, List, Optional
from car import Car

Coordinates = Tuple[int, int]
EMPTY_CELL_IN_BOARD = "_"
EXIT_CELL_IN_BOARD = "E"
BOARD_ROWS = 7
BOARD_COLS = 7
EXIT_LOCATION_IN_BOARD = (BOARD_ROWS // 2, BOARD_COLS)

class Board:
    """
    This class represents a board for rush-hour game, every board has:
    Board - a matrix (2-dimensional array) of strings
    Cars - list of all the cars in the board 
    """
    def __init__(self) -> None:
        """
        A constructor for a Board object.
        """
        self.__board = self.__create_board()
        self.__cars = {} #type: ignore

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        board_to_print = ""
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if (row, col) == EXIT_LOCATION_IN_BOARD:
                    board_to_print += EXIT_CELL_IN_BOARD
                elif col == len(self.__board[row]):
                    if self.__board[row][col]:
                        board_to_print += self.__board[row][col] + " *"
                    else:
                        board_to_print += EMPTY_CELL_IN_BOARD + " *"
                else:
                    if self.__board[row][col]:
                        board_to_print += self.__board[row][col] + " "
                    else:
                        board_to_print += EMPTY_CELL_IN_BOARD + " "
            board_to_print += "\n" # next line after last col each line
        return board_to_print

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        coordinates_of_board = []
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                coordinates_of_board.append((row, col))
        return coordinates_of_board

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """ 
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        possible_moves_list = [] #type: ignore
        for car in self.__cars.items():
            for move in car[1].possible_moves().items():
                move_key = move[0]
                description = move[1]
                name_of_car = car[1].get_name()
                if car[1].movement_requirements(move_key)[0] in self.__get_empty_coordinates_in_board():
                    possible_moves_list.append((name_of_car, move_key, description))
        return possible_moves_list

    def target_location(self) -> Coordinates:
        """
        This function returns the coordinates of the location that should be 
        filled for victory.
        :return: (row, col) of the goal location.
        """
        return EXIT_LOCATION_IN_BOARD

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        if not self.__board[coordinates[0]][coordinates[1]]: # empty cell
            return None
        return self.__board[coordinates[0]][coordinates[1]]
        
    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        if not self.__is_name_valid(car): # name is not valid, can't add to the board
            return False
        car_coordinates = car.car_coordinates()
        for coordinate in car_coordinates: # check validity of all coordinates of the car
            if self.__is_coordinate_out_of_board(coordinate):
                return False
            if self.cell_content(coordinate) is not None: # coordinate is not empty, can't add to the board
                return False
        name = car.get_name()
        self.__cars.update({name: car})
        self.__update_board() # update the board after the changes
        return True # if got here, the board changed 

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        for move in self.possible_moves():
            if (name, move_key) == (move[0], move[1]): # if the car can move
                self.__cars.get(name).move(move_key) #type:ignore 
                # get the car by his name and move it with move_key type:ignore
                self.__update_board()
                return True 
        return False # If got here, the car can't move

    # PRIVATE FUNCTIONS

    def __get_empty_coordinates_in_board(self) -> List[Coordinates]:
        """
        Returns all the empty coordinates in the board (there is no car on this coordinate)
        :return: list of empty coordinates
        """
        empty_coordinates = []
        for cell in self.cell_list():
            if not self.__board[cell[0]][cell[1]]: # empty coordinate
                empty_coordinates.append(cell)
        return empty_coordinates

    def __is_name_valid(self, car: Car) -> bool:
        """
        Checks if name of car is valid to add to the board
        :param car: a car
        :return: True if valid, False else
        """
        name_of_curr_car = car.get_name()
        if name_of_curr_car.upper() != name_of_curr_car: # car name wasn't uppercase
            return False
        if len(name_of_curr_car) != 1: # car name is not one char
            return False
        if not name_of_curr_car.isalpha(): # car name is not an english char
            return False            
        for car_in_board in self.__cars:
            if car_in_board == name_of_curr_car: # name already in board
                return False
        return True

    def __create_board(self) -> List[List]:
        """
        Create a board 7x7 and one exit coordinate in (3,7)
        :return: board
        """
        board = []
        board_row = [] #type: ignore
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board_row.append([])
            board.append(board_row)
            board_row = []
        board[EXIT_LOCATION_IN_BOARD[0]].append([]) 
        return board

    def __update_board(self) -> None:
        """
        Update a board by new coordinates of cars
        """
        updated_board = self.__create_board() # Create a new board, which will be the updated
        for car in self.__cars.items():
            curr_car = car[1]
            for car_coordinate in curr_car.car_coordinates():
                updated_board[car_coordinate[0]][car_coordinate[1]] = curr_car.get_name()
        self.__board = updated_board # update the board of the class

    def __is_coordinate_out_of_board(self, coordinate: Coordinates) -> bool:
        """
        Checks if a coordinate is out of the board
        :param coordinate: a coordinate
        :return: True if valid, False else
        """
        row, col = coordinate
        if row < 0 or col < 0 or row >= BOARD_ROWS or col >= BOARD_COLS:
            if (row, col) == self.target_location(): # if it's the target location it's ok
                return False
            return True
        return False
