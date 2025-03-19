#################################################################
# FILE : wordsearch_test.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex5 2025
# DESCRIPTION: In this file I made some tests for wordsearch program 
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: sys.exit usage - None
# NOTES: None
#################################################################
# This is constant file names that the tests use 
WORDLIST_TESTER_FILE_NAME = 'read_wordlist_tester.txt'
MATRIX_TESTER_FILE_NAME = "read_matrix_tester.txt"
WRITE_OUTPUT_TESTER_FILE_NAME = "write_output_tester.txt"
# This is output messages to the user 
ERROR_MSG_FOR_READ_WORDLIST_TESTER = "The return value from the function read_wordlist() is invalid.\nInput: file with content: "
ERROR_MSG_FOR_READ_MATRIX_TESTER = "The return value from the function read_matrix() is invalid.\nInput: file with content: "
ERROR_MSG_FOR_FIND_WORDS_TESTER = "The return value from the function find_words() is invalid.\nInput: "
ERROR_MSG_FOR_WRITE_OUTPUT_TESTER = "The file content that the function write_output() wrote is invalid.\nInput: "
ERROR_MSG_FOR_COUNT_EXISTANCE_OF_SUBSTRING_IN_STRING = "The return value from the function count_existance_of_substring_in_string() is invalid.\nInput: "
ERROR_MSG_FOR_REMOVE_DOUBLES_FROM_LIST = "The return value from the function remove_doubles_from_list() is invalid.\nInput: "

import wordsearch
import os

def test_read_wordlist() -> None:
    """
    This function is a test to read_wordlist from wordsearch.py
    The function tests three sceanrios of inputs and will raise an informative assert error if there is a a problem 
    """
    words = [["apple", "table", "sink", "puzzle", "messi", "meadow", "israel", "whisp"], [""], ["word"]]
    tester_file = open(WORDLIST_TESTER_FILE_NAME, 'w')
    tester_file.writelines("\n".join(words[0]))
    tester_file.close()
    try:
        assert wordsearch.read_wordlist(WORDLIST_TESTER_FILE_NAME) == words[0], f"{ERROR_MSG_FOR_READ_WORDLIST_TESTER}{words[0]}"
    finally:
        os.remove(WORDLIST_TESTER_FILE_NAME)
    tester_file = open(WORDLIST_TESTER_FILE_NAME, 'w')
    tester_file.writelines(words[1])
    tester_file.close()
    try:
        assert wordsearch.read_wordlist(WORDLIST_TESTER_FILE_NAME) == [], f"{ERROR_MSG_FOR_READ_WORDLIST_TESTER}No content"
    finally:
        os.remove(WORDLIST_TESTER_FILE_NAME)
    tester_file = open(WORDLIST_TESTER_FILE_NAME, 'w')
    tester_file.writelines(words[2])
    tester_file.close()
    try:
        assert wordsearch.read_wordlist(WORDLIST_TESTER_FILE_NAME) == words[2], f"{ERROR_MSG_FOR_READ_WORDLIST_TESTER}{words[2]}"
    finally:
        os.remove(WORDLIST_TESTER_FILE_NAME)

def test_read_matrix() -> None:
    """
    This function is a test to read_matrix from wordsearch.py
    The function tests three scenarios of inputs and will raise an informative assert error if there is a problem
    """
    matrix = [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]
    tester_file = open(MATRIX_TESTER_FILE_NAME, 'w')
    tester_file.writelines(",".join(row) + "\n" for row in matrix)
    tester_file.close()
    try:
        assert wordsearch.read_matrix(MATRIX_TESTER_FILE_NAME) == matrix, f"{ERROR_MSG_FOR_READ_MATRIX_TESTER}{matrix}"
    finally:
        os.remove(MATRIX_TESTER_FILE_NAME)
    tester_file = open(MATRIX_TESTER_FILE_NAME, 'w')
    tester_file.writelines([""])
    tester_file.close()
    try:
        assert wordsearch.read_matrix(MATRIX_TESTER_FILE_NAME) == [], f"{ERROR_MSG_FOR_READ_MATRIX_TESTER}{[]}"
    finally:
        os.remove(MATRIX_TESTER_FILE_NAME)
    tester_file = open(MATRIX_TESTER_FILE_NAME, 'w')
    tester_file.write('a,b,c')
    tester_file.close()
    try:
        assert wordsearch.read_matrix(MATRIX_TESTER_FILE_NAME) == [['a', 'b', 'c']], f"{ERROR_MSG_FOR_READ_MATRIX_TESTER}a,b,c"
    finally:
        os.remove(MATRIX_TESTER_FILE_NAME)

def test_find_words_longer_than_matrix() -> None:
    """
    This function is a test to find_words() from wordsearch.py
    The function tests several scenarios of inputs with words that longer than the matrix and will raise an informative assert error if there is a problem
    """
    matrix = [["a","p","p","l","e"], ["a","g","o","d","o"], ["n","n","e","r","t"], ["g","a","T","A","C"], ["m","i","c","s","r"], ["P","o","P","o","P"]]
    words = ["example", "discover", "celebrate"]
    directions = ["ldr", "wxy", "l", "udlrxyzw", "w", "xy"]
    for direction in directions:
        assert wordsearch.find_words(words, matrix, direction) == [], f"{ERROR_MSG_FOR_FIND_WORDS_TESTER}\nMatrix: {matrix}\nWords: {words}\nDirections: {direction}"
    words = ["dog", "checker", "god"]
    directions = ["lr", "rl"]
    for direction in directions:
        assert wordsearch.find_words(words, matrix, direction) == [("dog", 1), ("god", 1)] or wordsearch.find_words(words, matrix, direction) == [("god", 1), ("dog", 1)], \
            f"{ERROR_MSG_FOR_FIND_WORDS_TESTER}\nMatrix: {matrix}\nWords: {words}\nDirections: {direction}"

def test_find_words_repeated_multiple_times() -> None:
    """
    This function is a test to find_words() from wordsearch.py
    The function tests some scenarios of inputs that repeated in the matrix and will raise an informative assert error if there is a problem
    """
    matrix = [['W', 'O', 'R', 'D', 'S', 'A'], ['T', 'E', 'S', 'T', 'E', 'R'], ['H', 'W', 'O', 'R', 'D', 'S'], ['F', 'I', 'N', 'D', 'E', 'D'], ['P', 'Y', 'T', 'H', 'O', 'N']]
    words = ["WORDS", "FINDED"]
    direction = "lr"
    assert wordsearch.find_words(words, matrix, direction) == [("WORDS", 2), ("FINDED", 1)] or wordsearch.find_words(words, matrix, direction) == [("FINDED", 1), ("WORDS", 2)], \
          f"{ERROR_MSG_FOR_FIND_WORDS_TESTER}\nMatrix: {matrix}\nWords: {words}\nDirections: {direction}"

def test_find_words_no_matches() -> None:
    """
    This function is a test to find_words() from wordsearch.py
    The function tests some scenarios of inputs that has no matches in the matrix and will raise an informative assert error if there is a problem
    """
    matrix = [['C', 'O', 'D', 'I', 'N', 'G'], ['L', 'E', 'A', 'R', 'N', 'S'], ['P', 'R', 'O', 'J', 'E', 'C'], ['M', 'A', 'T', 'R', 'I', 'X'], ['F', 'U', 'N', 'C', 'T', 'S']]
    words = ["CODER", "PROJECTS"]
    direction = "lrwxyz"
    assert wordsearch.find_words(words, matrix, direction) == [], f"{ERROR_MSG_FOR_FIND_WORDS_TESTER}\nMatrix: {matrix}\nWords: {words}\nDirections: {direction}"

def test_write_output() -> None:
    """
    This function is a test to write_output() from wordsearch.py
    The function tests some scenarios of inputs and will raise an informative error if there is a problem
    """
    results: list = []
    try:
        wordsearch.write_output(results, WRITE_OUTPUT_TESTER_FILE_NAME)
        with open(WRITE_OUTPUT_TESTER_FILE_NAME, 'r') as tester:
            if len(tester.read()) != 0:
                raise Exception(f"{ERROR_MSG_FOR_WRITE_OUTPUT_TESTER}{results}")
    finally:
        os.remove(WRITE_OUTPUT_TESTER_FILE_NAME)
    results = [("word", 5)]
    try:
        wordsearch.write_output(results, WRITE_OUTPUT_TESTER_FILE_NAME)
        with open(WRITE_OUTPUT_TESTER_FILE_NAME, 'r') as tester:
            if tester.read() != "word,5\n":
                raise Exception(f"{ERROR_MSG_FOR_WRITE_OUTPUT_TESTER}{results}")
    finally:
        os.remove(WRITE_OUTPUT_TESTER_FILE_NAME)

def test_count_substring_existance() -> None:
    """
    This function is a test to count_existance_of_substring_in_string() from wordsearch.py
    The function tests some scenarios of inputs and will raise an informative assert error if there is a problem
    """
    subst = "PoP"
    word = "PoPoPoPoP"
    assert wordsearch.count_existance_of_substring_in_string(subst, word) == 4, f"{ERROR_MSG_FOR_COUNT_EXISTANCE_OF_SUBSTRING_IN_STRING}\nSubstring: {subst}\nWord: {word}"
    subst = "Afek"
    word = "AfekCodedThisFileAndAfekCodedTheSecondFile"
    assert wordsearch.count_existance_of_substring_in_string(subst, word) == 2, f"{ERROR_MSG_FOR_COUNT_EXISTANCE_OF_SUBSTRING_IN_STRING}\nSubstring: {subst}\nWord: {word}"

def test_remove_doubles_from_list() -> None:
    """
    This function is a test to remove_doubles_from_list() from wordsearch.py
    The function tests some scanrios of inputs and will raise an informative assert error if there is a problem
    """
    lst_of_occurences = [("Afek", 4), ("Afek", 3), ("Afek", 2)]
    assert wordsearch.remove_doubles_from_list(lst_of_occurences) == [("Afek", 9)], f"{ERROR_MSG_FOR_REMOVE_DOUBLES_FROM_LIST}\nList: {lst_of_occurences}"
    lst_of_occurences = [("Afek", 2), ("CSE", 3), ("Afek", 2), ("EX5", 2)]
    assert wordsearch.remove_doubles_from_list(lst_of_occurences) == [("Afek", 4), ("CSE", 3), ("EX5", 2)], f"{ERROR_MSG_FOR_REMOVE_DOUBLES_FROM_LIST}\nList: {lst_of_occurences}"