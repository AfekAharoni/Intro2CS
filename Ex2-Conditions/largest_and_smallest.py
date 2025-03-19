#################################################################
# FILE : largest_and_smallest.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex2 2025
# DESCRIPTION: In this file there are 2 functions, one that checks max and min values in 3 numbers, and the other that checks the first
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: I chose the args (-1, 0, 1) because one negative, one positive and one zero
# NOTES: I chose the args (0, 0, 0) because they're all the same number, and the function doesn't get inside the condition
#################################################################

def largest_and_smallest(num1, num2, num3):
    """
    This function get 3 numbers -> num1, num2, num3
    The function returns the maximum value and the minimum value of these three
    The function returns the maximum first and the minimum second
    The function assumes that num1, num2 and num3 are numbers
    The function doesn't use the functions min, max or sort
    """
    max_val = num1 # set the max_val as the first number
    min_val = num1 # set the min_val as the first number
    if num2 > max_val: # if the second number is bigger than the first one
        max_val = num2
    elif num2 < min_val: # if the second number is lower than the first one
        min_val = num2
    if num3 > max_val: # if the third number is bigger than max_value
        max_val = num3
    elif num3 < min_val: # if the third number is lower than min_value
        min_val = num3 
    return max_val, min_val

def check_largest_and_smallest():
    """
    This function checks the function 'largest_and_smallest'
    The function tries 5 times the function above, and check if the values returned correct
    If they're not correct, the function returns False
    If they're all correct, the function returns True
    """
    max_val, min_val = largest_and_smallest(17, 1, 6)
    if max_val != 17 or min_val != 1:
        return False
    max_val, min_val = largest_and_smallest(1, 17, 6)
    if max_val != 17 or min_val != 1:
        return False
    max_val, min_val = largest_and_smallest(1, 1, 2)
    if max_val != 2 or min_val != 1:
        return False
    max_val, min_val = largest_and_smallest(-1, 0, 1)
    if max_val != 1 or min_val != -1:
        return False
    max_val, min_val = largest_and_smallest(0, 0, 0)
    if max_val != 0 or min_val != 0:
        return False
    return True