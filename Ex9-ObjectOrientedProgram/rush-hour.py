#################################################################
# FILE : rush-hour.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex9 2025
# DESCRIPTION: In this file I made the implement rush-hour game using car, board and game classes
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################

import sys
from helper import *
from game import *
from car import *

OPTIONS_FOR_ORIENTATION = [0, 1]
CAR_IN_TARGET = "There is a car in the target location, so the game is over!"

def check_validity_of_name(name: str) -> bool:
    """
    This function gets a name and return if the name is valid to be inserted to the board
    """
    if name != name.upper(): # car name wasn't uppercase
        return False
    if len(name) != 1: # car name is not one charachter
        return False
    if not name.isalpha(): # car name is not an english charachter 
        return False
    return True

if __name__ == "__main__":
    # In the exercise instructions, it said I can assume that the argv is valid and the file path is valid
    json_file_path = sys.argv[1]
    board = Board()
    json_content = load_json(json_file_path)
    for item in json_content.items():
        try:
            name_of_car = item[0]
            if check_validity_of_name(name_of_car):
                length_of_car = item[1][0] # assumes that legal, larger than zero
                location_of_car = (item[1][1][0], item[1][1][1]) #type: ignore
                orientation_of_car = item[1][2]
                if orientation_of_car in OPTIONS_FOR_ORIENTATION:
                    car = Car(name_of_car, length_of_car, location_of_car, orientation_of_car) #type: ignore
                    board.add_car(car)
        except:
            continue
    if board.cell_content(board.target_location()) is None:
        game = Game(board)
        game.play()
    else:
        print(CAR_IN_TARGET)