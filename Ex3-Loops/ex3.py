#################################################################
# FILE : ex3.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex3 2025
# DESCRIPTION: In this file there are different functions for exercise 3
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Return statement on multiple lines - https://shorturl.at/ruGce
# NOTES: None
#################################################################


# Constants of each setting as in Exercise 3
INCREASING_MONOTONICITY = 0
STRICTED_INCREASING_MONOTONICITY = 1
DECREASING_MONOTONICITY = 2
STRICTED_DECREASING_MONOTONICITY = 3

def input_list():
    """
    This function gets numbers as an input from the user, until the user choose "" (empty)
    The function returns list of the inputs, as floats.
    The last number in the list is the summary of all the numbers before him.
    Every single cell contains one input, the last input ("") is not in the list
    If the first input is "", the function returns list with single cell, 0 -> [0]
    The function assumes that the user chose only numbers or ""
    The function doesn't use the sum() function
    """
    input_list_of_nums = [] # Set a list that will be return with numbers
    number_chosen_by_user = input() # Get the first input
    if number_chosen_by_user == "": # If the first input was "", the function returns one cell with 0
        return [0]
    else:
        number_chosen_by_user = float(number_chosen_by_user) # Change the input to float
        while number_chosen_by_user != "": # If the input was "", there will be no more iterations in the while loop
            input_list_of_nums.append(float(number_chosen_by_user)) # Add the input to the end of the list
            number_chosen_by_user = input() # Get another input
    sum = 0
    for i in range(len(input_list_of_nums)): # This for loop runs all over the indexes of the list
        sum += input_list_of_nums[i] # Add the num to sum
    input_list_of_nums.append(sum) # Add the sum to the list
    return input_list_of_nums # Returns the list

def inner_product(vec_1, vec_2):
    """
    This function gets two vectors (as 2 lists) and returns the inner product of them
    The function assumes that both vec_1 and vec_2 are two lists of numbers (int or float)
    If the length of them isn't the same, the function returns None
    If the length of both are 0, the function return 0
    """
    if len(vec_1) != len(vec_2): # If their length isn't the same, return None
        return None
    if len(vec_1) == 0: # If the function gets here, it means that the length of both vec_1 and vec_2 are the same
        # Could be if len(vec_2) == 0:
        return 0
    sum = 0 # Set a variable to be the inner product that will be returned
    for i in range(len(vec_1)): # could be range(len(vec_2)) because they're the same length
        sum += (vec_1[i] * vec_2[i]) # Add to the sum the inner product of each index
    return sum # Return the inner product

def check_increasing_monotonicity(sequence):
    """
    This function gets sequence and check if it's increasing monotonicity sequence
    If not, the function returns False
    """
    for i in range(1, len(sequence)): # Runs all over the sequence from index 1, to the end
        if sequence[i] < sequence[i-1]:
            return False # It's not an increasing monotonicity sequence
    return True

def check_stricted_increasing_monotonicity(sequence):
    """
    This function gets sequence and check if it's stricted increasing monotonicity sequence
    If not, the function returns False
    """
    for i in range(1, len(sequence)): # Runs all over the sequence from index 1, to the end
        if sequence[i] <= sequence[i-1]:
            return False # It's not a stricted increasing monotonicity sequence
    return True

def check_decreasing_monotonicity(sequence):
    """
    This function gets sequence and check if it's decreasing monotonicity sequence
    If not, the function returns False
    """
    for i in range(1, len(sequence)): # Runs all over the sequence from index 1, to the end
        if sequence[i] > sequence[i-1]:
            return False # It's not a decreasing monotonicity sequence
    return True

def check_stricted_decreasing_monotonicity(sequence):
    """
    This function gets sequence and check if it's stricted decreasing monotonicity sequence
    If not, the function returns False
    """
    for i in range(1, len(sequence)): # Runs all over the sequence from index 1, to the end
        if sequence[i] >= sequence[i-1]:
            return False # It's not a stricted decreasing monotonicity sequence
    return True

def sequence_monotonicity(sequence):
    """
    This function gets a sequence and check it's 4 possibles monotonicity:
    Increasing monotonicity, Stricted Increasing monotonicity, Decreasing monotonicity and Stricted Decreasing monotonicity
    The function returns list in length of 4, and each cell is a boolean, True or False
    that represents the monotonicity in the order above
    The function assumes that 'sequence' is a list of numbers (int or float)
    The function uses other functions:
        1. check_increasing_monotonicity - checks if the sequence is an increasing monotonicity
        2. check_stricted_increasing_monotonicity - checks if the sequence is a stricted increasing monotonicity
        3. check_decreasing_monotonicity - checks if the sequence is a decreasing monotonicity
        4. check_stricted_decreasing_monotonicity - checks if the sequence is a stricted decreasing monotonicity
    This function doesn't use all or any functions
    In general, the function returns a list like that -> [True/False, True/False, True/False, True/False]
    If the length of the sequence if 0 or 1, the function will return [True, True, True, True]
    """
    monotonicity_list = [True, True, True, True]
    if len(sequence) == 0 or len(sequence) == 1: # If the length of the sequence is 0 or 1
        return monotonicity_list # [True, True, True, True]
    monotonicity_list[INCREASING_MONOTONICITY] = check_increasing_monotonicity(sequence)
    monotonicity_list[STRICTED_INCREASING_MONOTONICITY] = check_stricted_increasing_monotonicity(sequence)
    monotonicity_list[DECREASING_MONOTONICITY] = check_decreasing_monotonicity(sequence)
    monotonicity_list[STRICTED_DECREASING_MONOTONICITY] = check_stricted_decreasing_monotonicity(sequence)
    return monotonicity_list

def filter_list(num_list, operator, number):
    """
    This function gets 3 arguments:
    num_list - one dimensional list
    operator - mathematical operator
    number - a number
    The function returns one dimensional list that contains only the elements that in the condition
    The function doesn't assume that the list isn't empty
    The function assumes that 'operator' is '>', '<' or '=' and nothing else
    The function doesn't use filter function
    """
    all_elements_in_condition = []
    if len(num_list) == 0: # If the length of the num_list is 0
        return all_elements_in_condition # Returns []
    for i in range(len(num_list)):
        if operator == "<" and num_list[i] < number:
            all_elements_in_condition.append(num_list[i])
        elif operator == ">" and num_list[i] > number:
            all_elements_in_condition.append(num_list[i])
        elif operator == "=" and num_list[i] == number: # From the assumption of the correction of the operator's value, operator == "="
            all_elements_in_condition.append(num_list[i])
    return all_elements_in_condition

def cycle_sublist(lst, start, step):
    """
    This function gets 3 arguments:
    lst - 1 dimensional list
    start - index of the list
    step - the step size we jump inside the list
    The function runs in the list, from the start index in jumps of step size, cycled inside the list
    Until it goes over the start index or at it
    The function returns a list of all the elements in the indexes as above
    The function assumes that start is a correct index that pointing to existing place in the list
    The function assumes that step is an integer > 0
    The function doesn't use slicing
    """
    sub_list = [] # The sublist that will be returned
    curr_index = start # The current index is the start index
    is_after_cycle = False # This boolean represent if we already did 1 cycle at the list or not, the default is not (False)
    while is_after_cycle == False or curr_index < start:
        # The loop runs only if one of the terms is True
        # If is_after_cycle is False, it means we can keep jump at the indexes, because we hadn't done one cycle
        # If curr_index < start, it means we can keep jump at the indexes, because we didn't reach the 'maximum point' of the steps
        # If one of the terms is still True, we can keep jumping
        sub_list.append(lst[curr_index]) # Add the element of the current index to the sub_list
        curr_index += step # Jump one more step
        if step > len(lst): # If the step will go over the list more than one time in step, break
            break
        if curr_index > len(lst)-1: # If the index, after the step added, is bigger than the length of the list -> len(lst)-1
            if curr_index >= start and is_after_cycle: # If inside the current iteration, we reach the 'maximum point' of the steps after one cycle, exit the loop
                break
            is_after_cycle = True # We did one cycle at the list
            curr_index = curr_index % len(lst) # The curr_index need to be inside the indexes of the list, in cycling
    return sub_list # Return the list with the elements needed

def convolve(mat):
    """
    This function gets 1 argument, mat - 2-dimensional list
    The function create new mat (2-dimensional list) by the elements in the mat given
    Every element in the new mat will be calculated with this formula:
    Row = i, column = j
    mat[i][j] + mat[i + 1][j] + mat[i + 2][j] + mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j + 1] + mat[i][j + 2] + mat[i + 1][j + 2] + mat[i + 2][j + 2]
    The function 'mat_summer' do this specific calculation, and this function uses 'mat_summer'
    The function checks if the mat is empty, if so - return None
    The function assumes that the argument given is list of lists (mat)
    The function assumes that every element in the mat given, is number (int/float)
    The function assumes that the mat given, is at least 3x3 (size)
    """
    if len(mat) == 0: # If the mat's length is 0, return None
        return None
    row_list = [] # List that will represent the row at the sum that'll be return
    total_mat = [] # The mat that will be return
    for row in range(len(mat)-2):
        """
        Run every row until length of the mat minus 2 because we take every row, row+1 and row+2
        Same about the columns, so we don't want the index to be out of range
        """
        for column in range(len(mat[row])-2):
            row_list.append(mat_summer(mat, row, column)) # Add the sum of the 9 elements needed
        total_mat.append(row_list) # Add the row to the final mat
        row_list = [] # Reset the row list, because we're moving to the next row
    return total_mat # Return the mat

def mat_summer(mat, row, column):
    """
    This function gets 3 arguments:
    mat - 2-dimensional list (list of lists)
    row & column - the indexes of the list that represent the row and the column
    The function calculates the sum from mat[row][column] to mat[row+2][column+2] and return it
    The function is called by 'convolve' so the assumption is the indexes are in range of the mat and all the assumptions of 'convolve'
    """
    return mat[row][column] + mat[row + 1][column] + mat[row + 2][column] + \
         mat[row][column + 1] + mat[row + 1][column + 1] + mat[row + 2][column + 1] + \
            mat[row][column + 2] + mat[row + 1][column + 2] + mat[row + 2][column + 2]

def num_of_orthogonal(vectors):
    """
    This function get 1 argument
    vectors - a list of vectors (list of lists)
    The function check how many orthogonal vectors are in the list
    In other words, the function checks every couple of vectors 1 time, if their inner product is 0, they're orthogonal
    The function returns the number of orthogonal all over the vectors list
    The function assumes that the argument given is a list
    The function assumes that the vectors has the same length and their elements are only numbers(int/float)
    The function uses 'inner_product' function that returns the inner product of two vectors
    """
    sum_of_orthogonal = 0
    for i in range(len(vectors)): # Run all the vectors
        for j in range(i+1, len(vectors)): # For every vector, run from the next vector until the end, so every couple of vectors are being checked one time only
            if inner_product(vectors[i], vectors[j]) == 0: # If they're orthogonal
                sum_of_orthogonal += 1
    return sum_of_orthogonal

