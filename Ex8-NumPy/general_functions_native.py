#################################################################
# FILE : general_functions_native.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex8 2025
# DESCRIPTION: In this file I made some basic functions on matrix without numpy
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Matrix multipication - Wiki - https://shorturl.at/35AjN
#                   Invertible Matrix - Wiki - https://tinyurl.com/4btcnp6j 
#                   Unit Matrix - Wiki - https://tinyurl.com/mwh3m83z
# NOTES: None
#################################################################

from typing import List

def list_equal(A:List[List[float]], B:List[List[float]], eps=1e-6) -> bool:
    """
    This function gets two matrix and checks whether the dimension of the matrix are same
    and if the abs of every values in same indexes is lower than eps given (default 1e-6)
    The function assumes that the inner lists have the same length, and the lists is list of lists of float
    The function returns True if the two conditions True, and False else
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]): # different dimensional
        return False
    for row in range(len(A)): # could be len(B)
        for col in range(len(A[0])): # could be len(B[0])
            if abs(A[row][col] - B[row][col]) > eps: # if there is a difference that bigger than eps
                return False
    return True

def sum_matrix_native(A:List[List[float]], axis:int)->List[float]:
    """
    This function gets a matrix and a number
    If axis is zero, the function returns list of sums for each column
    If axis is one, the function returns lists of sums for each row
    The function assumes that axis is zero or one
    """
    list_of_sums = []
    sum = 0.0
    if axis == 0:
        for col in range(len(A[0])):
            for row in range(len(A)):
                sum += A[row][col]
            list_of_sums.append(sum)
            sum = 0.0
    elif axis == 1:
        for row in range(len(A)):
            for col in range(len(A[row])):
                sum += A[row][col]
            list_of_sums.append(sum)
            sum = 0.0
    return list_of_sums

def mul_mat_native(A: List[List[float]], B:List[List[float]])-> List[List[float]]:
    """
    This function gets two matrix and return the multipication matrix of them
    If there dimensions incompatible, a ValueError will raise
    """
    if len(A[0]) != len(B): # ths number of columns in A needs to be the number of rows in B   
        raise ValueError("Matrix dimensions are incompatible")
    sum = 0.0
    mul_mat = []
    row_of_mul_mat = []
    for row in range(len(A)): # for every row in A
        for col in range(len(B[0])): # for every column in B
            for index_to_mul in range(len(A[row])): # for every column in B
                sum += A[row][index_to_mul] * B[index_to_mul][col]
            row_of_mul_mat.append(sum)
            sum = 0.0
        mul_mat.append(row_of_mul_mat)
        row_of_mul_mat = []
    return mul_mat

def create_identity_matrix(size: int):
    """
    This function gets a size and return the identity matrix in sizes: size X size
    """
    identity_matrix = []
    row_in_identity_matrix = []
    for row in range(size):
        for col in range(size):
            if row == col:
                row_in_identity_matrix.append(1)
            else:
                row_in_identity_matrix.append(0)
        identity_matrix.append(row_in_identity_matrix)
        row_in_identity_matrix = []
    return identity_matrix

def is_inverse_native(A:List[List[float]], B:List[List[float]]) -> bool:
    """
    This function gets two matrix and returns whether the one inversed by the other
    """
    result = mul_mat_native(A, B)
    if list_equal(result, create_identity_matrix(len(A))):
        return True
    return False 
