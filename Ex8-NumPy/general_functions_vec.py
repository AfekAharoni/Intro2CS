#################################################################
# FILE : general_functions_vec.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex8 2025
# DESCRIPTION: In this file I made some basic functions on matrix using numpy
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Numpy: the absolute basics for beginners - https://shorturl.at/4fnrS
#                   numpy.any usage - https://shorturl.at/cROjz
#                   numpy.any usage - https://shorturl.at/YAi9q
#                   Matrix multipication - Wiki - https://shorturl.at/35AjN
#                   numpy.matmul() usage - https://shorturl.at/PyeuE
#                   Invertible Matrix - Wiki - https://tinyurl.com/4btcnp6j 
#                   Unit Matrix - Wiki - https://tinyurl.com/mwh3m83z
# NOTES: None
#################################################################

import numpy
import numpy.linalg

def ndarray_equal(A: numpy.ndarray, B: numpy.ndarray, eps=1e-6) -> bool:
    """
    This function gets two matrix and checks whether the dimension of the matrix are same
    and if the abs of every values in same indexes is lower than eps given (defaultive 1e-6)
    The function returns True if the two conditions True, and False else
    The function using numpy 
    """
    if A.shape != B.shape: # different dimensional
        return False
    absolute_difference_A_and_B = numpy.absolute(A - B) # create a new array of the absolute differences between each value
    if numpy.any(absolute_difference_A_and_B > eps): # if there is a difference that bigger or equal to eps
        return False
    return True

def sum_matrix_vec(A: numpy.ndarray, axis: int) -> numpy.ndarray:
    """
    This function gets a matrix and a number
    If axis is zero, the function returns list of sums for each column
    If axis is one, the function returns lists of sums for each row
    The function assumes that axis is zero or one
    This function using numpy
    """
    return numpy.array(numpy.sum(A, axis))

def mul_mat_vec(A: numpy.ndarray, B: numpy.ndarray)-> numpy.ndarray:
    """
    This function gets two matrix and return the multipication matrix of them
    If there dimensions incompatible, a ValueError will raise
    This function using numpy
    """
    if A.shape[1] != B.shape[0]: # Dimensions invalid for multipication
        raise ValueError("Matrix dimensions are incompatible")
    return numpy.matmul(A,B)
    
def is_inverse_vec(A:numpy.ndarray, B:numpy.ndarray) -> bool:
    """
    This function gets two matrix and returns whether the one inversed by the other
    This function using numpy
    """
    try:
        if ndarray_equal(numpy.linalg.inv(A), B) and ndarray_equal(numpy.linalg.inv(B), A):
            return True
    except:
        return False
    return False

