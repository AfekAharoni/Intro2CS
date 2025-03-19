#################################################################
# FILE : car.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex9 2025
# DESCRIPTION: In this file I made the car class for the game rush-hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################

from typing import Tuple, List, Dict

VERTICAL_ORIENTATION = 0
HORIZONTAL_ORIENTATION = 1
UP_DIRECTION = "u"
DOWN_DIRECTION = "d"
RIGHT_DIRECTION = "r"
LEFT_DIRECTION = "l"
VERTICAL_ORIENTATION_DIRECTION_DICT = {UP_DIRECTION: "Car is vertical so can move up", DOWN_DIRECTION: "Car is vertical so can move down"}
HORIZONTAL_ORIENTATION_DIRECTION_DICT = {RIGHT_DIRECTION: "Car is horizontal so can move right", LEFT_DIRECTION: "Car is horizontal so can move left"}


Coordinates = Tuple[int, int]

class Car:
    """
    This class represents a car, every car has:
    Name - the name of the car
    Length - The length of the car (size of the car in the board)
    Location - Top left corner of the car 
    Orientation - 0 represents vertical and 1 represent horizontal
    """
    def __init__(self, name: str, length: int, location: Coordinates, 
                 orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        list_of_coordinates = []
        for i in range(self.__length): # run self.__length times
            if self.__orientation == VERTICAL_ORIENTATION:
                list_of_coordinates.append((self.__location[0] + i, self.__location[1]))
            else: # self.__orientation == HORIZONTAL_ORIENTATION
                    list_of_coordinates.append((self.__location[0], self.__location[1] + i))
        return list_of_coordinates

    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this car.
        """
        if self.__orientation == VERTICAL_ORIENTATION:
            return VERTICAL_ORIENTATION_DIRECTION_DICT
        return HORIZONTAL_ORIENTATION_DIRECTION_DICT # self.__orientation == HORIZONTAL_ORIENTATION
            
    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for 
                 this move to be legal.
        """
        curr_location = self.__location
        car_length = self.__length
        moves_can_be_done = [] #type: ignore
        if move_key not in self.possible_moves():
            return moves_can_be_done
        if self.__orientation == VERTICAL_ORIENTATION: # If the orientation is vertical, the move_key can be up or down
            if move_key == UP_DIRECTION:
                moves_can_be_done.append((curr_location[0] - 1, curr_location[1]))
            elif move_key == DOWN_DIRECTION:
                moves_can_be_done.append((curr_location[0] + car_length, curr_location[1]))
        elif self.__orientation == HORIZONTAL_ORIENTATION: # If the orientation is horizontal, the move_key can be right or left
            if move_key == RIGHT_DIRECTION:
                moves_can_be_done.append((curr_location[0], curr_location[1] + car_length))
            elif move_key == LEFT_DIRECTION:
                moves_can_be_done.append((curr_location[0], curr_location[1] - 1))
        return moves_can_be_done
            
    def move(self, move_key: str) -> bool:
        """ 
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key not in self.possible_moves(): # Move key isn't valid
            return False
        moves_can_be_done = self.movement_requirements(move_key)
        if len(moves_can_be_done) == 0: # no moves can be done
            return False
        # new_location is the new location of the car after one move (top left corner)
        # new_location_to_check is the last coordinate the car need to move to (bottom right corner)
        if move_key == UP_DIRECTION:
            new_location = (self.__location[0] - 1,self.__location[1]) 
            new_location_to_check = new_location
        elif move_key == DOWN_DIRECTION:
            new_location = (self.__location[0] + 1, self.__location[1])
            new_location_to_check = (self.__location[0] + self.__length, self.__location[1])
        elif move_key == RIGHT_DIRECTION:
            new_location = (self.__location[0], self.__location[1] + 1)
            new_location_to_check = (self.__location[0], self.__location[1] + self.__length)
        elif move_key == LEFT_DIRECTION:
            new_location = (self.__location[0], self.__location[1] - 1)
            new_location_to_check = new_location
        if new_location_to_check not in moves_can_be_done:
            return False
        self.__location = new_location
        return True

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.__name
