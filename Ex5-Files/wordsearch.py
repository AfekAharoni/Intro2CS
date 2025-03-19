#################################################################
# FILE : wordsearch.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex5 2025
# DESCRIPTION: In this file I made a wordsearch program 
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: sys.exit usage - https://shorturl.at/UMOyp 
#                   dictionary item and value usage - https://shorturl.at/73uJm
#                   find() method usage - https://shorturl.at/S4VBJ 
# NOTES: None
#################################################################

# This is the directions as described in ex5
ALL_DIRECTIONS = "udrlwxyz"
U_DIRECTION = "u"
D_DIRECTION = "d"
R_DIRECTION = "r"
L_DIRECTION = "l"
W_DIRECTION = "w"
X_DIRECTION = "x"
Y_DIRECTION = "y"
Z_DIRECTION = "z"
# This is output messages to the user
NUM_OF_ARGS_NOT_VALID = "Invalid number of parameters, try with 4 parameters"
WORDS_FILE_PROBLEM = "Words file can't be read!"
MATRIX_FILE_PROBLEM = "Matrix file can't be read!"
CANT_WRITE_OR_OUTPUT_FILE_NAME_NOT_VALID = "Invalid name of output file or can't write there!"
DIRECTIONS_NOT_EXIST = "is invalid direction, valid directions: u,d,r,l,w,x,y,z only."

from copy import deepcopy
from typing import Union
import sys

def read_wordlist(filename: str) -> list[str]:
    """
    This function gets file name which contains list of words
    The function opens the file, reads the words inside him and returns list of the words
    """
    try:
        file = open(filename, 'r')
        word_list = file.readlines()
    except:
        sys.exit(WORDS_FILE_PROBLEM)
    for i in range(len((word_list))):
        if "\n" in word_list[i]: # remove \n from each word
            word_list[i] = word_list[i].replace("\n", "") 
    file.close()
    return word_list

def read_matrix(filename: str) -> list[list[str]]:
    """
    This function gets file name which contains matrix of letters
    The function opens the file, reads the matrix and returns 2 dimensional list with the letters
    """
    matrix = []
    row = []
    try:
        file = open(filename, 'r')
        for line in file.readlines():
            row = line.replace("\n", "").split(",") # removes \n from the word, and split by , to list
            matrix.append(row)
        file.close()
    except:
        sys.exit(MATRIX_FILE_PROBLEM)
    return matrix

def count_existance_of_substring_in_string(subst: str, word: str) -> int:
    """
    This function gets substring and a word, and search return how many times the substring is in word
    """
    subst_len = len(subst)
    counter = 0
    for index in range(len(word)):
        if word.find(subst, index, index+subst_len) != -1: # find will return -1 if there is no such subst in word
            # Search the specific substring in word, from the current index to the current index + length of the substring
            counter += 1
    return counter

def reverse_rows_in_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """
    This function gets a matrix and returns a reversed-rows matrix
    """
    new_matrix = deepcopy(matrix) # deep copy of the original matrix
    return new_matrix[::-1]

def reverse_columns_in_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """
    This function gets a matrix and returns a reversed-columns matrix
    """
    new_matrix = deepcopy(matrix) # deep copy of the original matrix
    for row in new_matrix: # run all over the rows
        row[:] = row[::-1] # reverse the row inside 
    return new_matrix

def reverse_column_and_rows_in_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """
    This function gets a matrix and returns a reversed-rows and reversed-columns matrix
    """
    new_matrix = deepcopy(matrix) # deep copy of the original matrix
    return reverse_rows_in_matrix(reverse_columns_in_matrix(new_matrix)) # could be reverse_columns_in_matrix(reverse_rows_in_matrix(new_matrix)) - its the same

def create_sequence_down(matrix: list[list[str]], column: int) -> str:
    """
    This function gets a matrix and a column, and returns the sequence of the letters in this column, as down the column
    """
    letter_sequence = "" # Initializing a sequence
    for row in range(len(matrix)): # Run from up to down
        letter_sequence += matrix[row][column] # Add letter to sequence
    return letter_sequence

def create_sequence_right(matrix: list[list[str]], row: int) -> str:
    """
    This function gets a matrix and a row, and returns the sequence of the letters in the row, from left to right at the row
    """
    letter_sequence = "" # Initializing a sequence
    for column in range(len(matrix[0])): # Run from left to right
        letter_sequence += matrix[row][column] # Add letter to sequence
    return letter_sequence

def create_sequence_slant(matrix: list[list[str]], row: int, column: int) -> str:
    """
    This function gets a matrix, a row and a column, and returns the sequence of the letters in y direction
    """
    letter_sequence = ""
    while row < len(matrix): # run all the rows until out of range
        while column < len(matrix[0]): # run all of the columns until out of range
            letter_sequence += matrix[row][column] # Add letter to sequence
            column += 1
            break # run one time per row, than jump to the next row
        row += 1
    return letter_sequence

def find_word_in_column(words: list[str], matrix:list[list[str]]) -> list[tuple[str, int]]:
    """
    This function gets list of words and a matrix and check how many times each word from the list
    Is in the columns of the matrix from up to down
    The function returns only the words that in the matrix at least one time
    """
    counter_per_word = []
    counter = 0
    columns_number = len(matrix[0]) # number of columns in the matrix
    for word in words:
        for column in range(columns_number): 
            letter_sequence = create_sequence_down(matrix, column) 
            counter += count_existance_of_substring_in_string(word, letter_sequence) # add the number of occurences of word in the letter sequence
            # add to the counter the number of occurences of word in letter_sequence
        if counter > 0: # if the word is in total at least one time, add that word and its counter to the list
            counter_per_word.append((word, counter))
        counter = 0 # reset the conter
    return counter_per_word

def find_word_in_row(words: list[str], matrix:list[list[str]]) -> list[tuple[str, int]]:
    """
    This function gets a list of words and a matrix and check how many times each word from the list
    Is in the rows of the matrix from left to right
    The function returns only the words that in the matrix at least one time
    """
    counter_per_word = []
    counter = 0
    for word in words:
        for row in range(len(matrix)):
            letter_sequence = create_sequence_right(matrix, row)
            counter += count_existance_of_substring_in_string(word, letter_sequence) # add the number of occurences of word in the letter sequence
            # add to the counter the number of occurences of word in letter_sequence
        if counter > 0:
            counter_per_word.append((word, counter))
        counter = 0
    return counter_per_word

def find_word_in_slant_direction(words: list[str], matrix: list[list[str]]) -> list[tuple[str, int]]:
    """
    This function gets a list of words and a matrix and check (by direction y - up to down left to right) how many times each word from the list
    Is in this direction
    The function returns only the words that in the matrix at least one time
    """
    counter_per_word = []
    counter = 0
    for word in words:
        for column in range(len(matrix[0]), -1, -1):
            letter_sequence = create_sequence_slant(matrix, 0, column) # the letters sequence we created in y direction
            counter += count_existance_of_substring_in_string(word, letter_sequence) # add the number of occurences of word in the letter sequence
            if counter > 0:
                counter_per_word.append((word, counter))
            counter = 0
        for row in range(1, len(matrix)): # run from 1 to the last row because 1 already checked 
            letter_sequence = create_sequence_slant(matrix, row, 0) # the letters sequence we created in y direction
            counter += count_existance_of_substring_in_string(word, letter_sequence) # add the number of occurences of word in the letter sequence
            if counter > 0:
                counter_per_word.append((word, counter))
            counter = 0
    return counter_per_word

def remove_doubles_from_list(lst_of_occurences: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    This function gets a list of tuple (str, int) and returns new list without double strings in the total tuple
    For example -> [("PoP", 2), ("PoP", 2)] will be [("PoP", 4)]
    """
    helper_dict: dict = dict() 
    new_list_of_occurences = []
    for index in range(len(lst_of_occurences)):
        if lst_of_occurences[index][0] not in helper_dict.keys(): # if this word is not in the dictionary yet
            helper_dict[lst_of_occurences[index][0]] = lst_of_occurences[index][1] # add the word ant its number
        else: # if the word already in the dictionary
            helper_dict[lst_of_occurences[index][0]] += lst_of_occurences[index][1] # add the curr number to the number in the dictionary
    for word, number in helper_dict.items():
        new_list_of_occurences.append((word, number)) # add every item from the dictionary to the list as tuple of key, value
    return new_list_of_occurences

def order_results_by_word_list(word_list: list[str], results: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    This function gets results and order them by the original word list
    """
    new_results = []
    for word in word_list:
        for result in results:
            if word == result[0]:
                new_results.append(result)
    return new_results

def find_words(word_list: list[str], matrix: list[list[str]], directrions: str) -> list[tuple[str, int]]:
    """
    This function gets word list, matrix and directions, and search each word from the list, as the directions given
    how many times in the matrix
    The function returns list of tuples - (word, how many times word in every directions total)
    """
    list_of_occurences_per_word = []
    if len(matrix) == 0:
        return []
    for letter in directrions:
        if letter == D_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_column(word_list, matrix))
        elif letter == U_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_column(word_list, reverse_rows_in_matrix(matrix)))
        elif letter == R_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_row(word_list, matrix))
        elif letter == L_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_row(word_list, reverse_columns_in_matrix(matrix)))
        elif letter == Y_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_slant_direction(word_list, matrix))
        elif letter == W_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_slant_direction(word_list, reverse_rows_in_matrix(matrix)))
        elif letter == Z_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_slant_direction(word_list, reverse_columns_in_matrix(matrix)))
        elif letter == X_DIRECTION:
            list_of_occurences_per_word.extend(find_word_in_slant_direction(word_list, reverse_column_and_rows_in_matrix(matrix)))
    return order_results_by_word_list(word_list, remove_doubles_from_list(list_of_occurences_per_word))

def write_output(results: Union[list[tuple[str, int]], list], filename: str) -> None:
    """
    This function gets results and a filename, and opens a file (or override file that has filename's name)
    The function write to the file, word, count for each result
    """
    try:
        with open(filename, 'w') as file:
            for result in results:
                file.write(f"{result[0]},{result[1]}\n")
    except:
        sys.exit(CANT_WRITE_OR_OUTPUT_FILE_NAME_NOT_VALID)

def removes_duplicates_from_string(directions: str) -> str:
    """
    This function gets a string of directions, and removes duplicated letters
    For example: "uddxyzy" -> "udxyz" (maybe not the same order)    
    """
    return "".join(set(directions))

def main(word_file: str, matrix_file: str, directions: str, output_file: str) -> None:
    try:
        word_list = read_wordlist(word_file)
    except:
        sys.exit(WORDS_FILE_PROBLEM)
    try:
        matrix = read_matrix(matrix_file)
    except:
        sys.exit(MATRIX_FILE_PROBLEM)
    for direction in directions:
        if direction not in ALL_DIRECTIONS: # direction isn't udrlwxyz
            sys.exit(f"{direction} {DIRECTIONS_NOT_EXIST}")
    directions = removes_duplicates_from_string(directions) # remove duplicates from directions
    if len(matrix) == 0: # If the matrix file was empty, create empty file
        write_output(matrix, output_file)
        sys.exit()
    try:
        results = find_words(word_list, matrix, directions)
        write_output(results, output_file)
    except:
        sys.exit(CANT_WRITE_OR_OUTPUT_FILE_NAME_NOT_VALID)


if __name__ == "__main__":
    if len(sys.argv) != 5: # 5 because: wordsearch.py, word_file, matrix_file, output_file, direction
        sys.exit(NUM_OF_ARGS_NOT_VALID)
    word_file = sys.argv[1]
    matrix_file = sys.argv[2]
    output_file = sys.argv[3]
    directions = sys.argv[4]
    main(word_file, matrix_file, directions, output_file)
