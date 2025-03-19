#################################################################
# FILE : ex7.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex7 2025
# DESCRIPTION: In this file I solved some problems with recursive
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Tower of Hanoi - Game - https://shorturl.at/FgN1U
#                   Tower of Hanoi - Wiki - https://shorturl.at/m4xIP
# NOTES: None
#################################################################

from typing import *
from ex7_helper import *
  
def mult(x: N, y: int) -> N:
    """
    This function gets a number (int or float) and a non-negative int and returns x*y in recursive
    The run time complexity of this function is O(y) (Linear)
    """
    if y == 0: # Base case
        return 0
    return add(x, mult(x, subtract_1(y)))

def is_even(n: int) -> bool:
    """
    This function gets a non-negative number and return True if he is even, and False else
    """
    if n == 0: # Base case - even
        return True
    if n == 1: # Base case - odd
        return False
    return is_even(subtract_1(subtract_1(n)))

def log_mult(x: N, y: int) -> N:
    """
    This function gets a number (int or float) and a non-negative int and returns x*y in recursive
    The run time complexity of this function is O(log(y)) (Logarithmic)
    """
    if y == 0: # Base case
        return 0
    half_result = log_mult(x, divide_by_2(y)) # Every number divide by two and calculate his mult in x
    if is_odd(y):
        return add(add(half_result, half_result), x)
    return add(half_result, half_result) # If got here, y is even so return twice the half

def is_power_helper(b: int, multer: int, x: int) -> bool:
    """
    This function is n helper function for is_power()
    The function gets two three non-negative numbers and return True if b is power of x and False else
    The function works recursively, and the run time complexity of this function is O(log(b)*log(x))
    """
    if multer > x: # so b is not power of x
        return False
    if multer == x: # so b is power of x
        return True
    return is_power_helper(b, log_mult(b, multer), x) # every run, mult (in logarithmic complexity) b and multer

def is_power(b: int, x: int) -> bool:
    """
    This function gets two non-negative numbers and returns True if b is power of x and False else
    The function works recursively, and the run time complexity of this function is O(log(b)*log(x))
    """
    if b == 0 and (x == 0 or x == 1):
        return True
    if b == 0:
        return False
    if x == 1: # Base case, b^0 == x for every b
        return True
    if b == 1: # Base case, 1^n == 1 for every n, and x is not 1 if got here
        return False
    return is_power_helper(b, b, x)

def reverse_helper(s: str, reversed_s: str, index: int):
    """
    This function gets two string and index, and add to the second string the first string in reverse
    The function works recursively
    """
    if index == 0: # Base case, 
        return append_to_end(reversed_s, s[0])
    return reverse_helper(s, append_to_end(reversed_s, s[index]), index - 1)

def reverse(s: str) -> str:
    """
    The function gets a string and returns its reversed string
    The function works recursively 
    """
    if s == "": # base case
        return ""
    return reverse_helper(s, "", len(s)-1) # len() is O(1)

def play_hanoi(Hanoi: Any, n: int, src: Any, dest: Any, temp: Any):
    """
    This function solved the hanoi game, the function works recursively and if the n given is non-positive number, the function "break"
    """
    if n <= 0:
        return # return None, just do nothing, "break"
    play_hanoi(Hanoi, n-1, src, temp, dest) # play with n-1 discs, from the src to the temp, using dest
    Hanoi.move(src, dest) # move the n (last one) disc from source to dest
    play_hanoi(Hanoi, n-1, temp, dest, src) # play with n-1 discs, from the temp to the dest, using src

def number_of_ones_helper(n: int) -> int:
    """
    The function return the number of ones in a number, works recursively
    """
    if n == 0: # base case
        return 0
    if n % 10 == 1: # add 1 to the result
        return 1 + number_of_ones_helper(n//10)
    return number_of_ones_helper(n//10)

def number_of_ones(n: int) -> int:
    """
    The function return the number of ones in all the number from 1 to n, works recursively with the helper function
    """
    if n <= 0: # base case, no ones in result
        return 0
    if n == 1: # base case
        return 1
    return number_of_ones(n-1) + number_of_ones_helper(n)

def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]], row: int, column: int) -> bool:
    """
    The function compares two lists and return True if they both the same, and False else
    """
    if row > len(l1) -1: # base case - end with all the rows
        return True
    if len(l1[row]) != len(l2[row]): # the lengths of the inner lists are different
        return False
    if column == len(l1[row]): # end with this row, go to the next row
        return compare_2d_lists_helper(l1, l2, row + 1, 0)
    if l1[row][column] != l2[row][column]: # different number
        return False
    return compare_2d_lists_helper(l1, l2, row, column + 1) # go to the next column

def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
    This function gets two list of lists and compares them
    """
    if len(l1) != len(l2): # the lengths are different
        return False
    if len(l1) == 0: # If got here, the lengths are the same, could be len(l2) == 0
        return True
    if len(l1[0]) != len(l2[0]): # If got here, there is at least one index (0) so it won't out of range
        return False
    return compare_2d_lists_helper(l1, l2, 0, 0)

def magic_list(n: int) -> List[Any]:
    """
    This function creates a magic list in recursive
    """
    if n == 0: # Base case
        return []
    lst = magic_list(n-1) # recursive call which creates a list in size (n-1)
    lst.append(magic_list(n-1)) # add to this list the last index, which size is (n-1)
    return lst

print(is_power(0, 1))