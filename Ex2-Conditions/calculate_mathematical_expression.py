#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex2 2025
# DESCRIPTION: In this file there are 2 functions that calculates mathematical expression from a string
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: split function explanation -> https://shorturl.at/ECqwy
# NOTES: None
#################################################################

def calculate_mathematical_expression(num1, num2, calc_type):
    """
    This function returns the calculation of  the expression by the arguments got.
    num1 is an int/float - number
    num2 is an int/float - number
    calc_type (str) is the type of the calculation the function needs to do,
    the options are: '+', '*', '-', ':'
    The function assumes that num1 and num2 are numbers and calc_type is a string.
    If the function got invalid command, it returns None
    """
    if calc_type == "+":
        return num1 + num2
    elif calc_type == "-":
        return num1 - num2
    elif calc_type == "*":
        return num1*num2
    elif calc_type == ":":
        if num2 == 0:
            return None # Can't divide by zero
        return num1/num2
    return None # If the function got here, calc_type is not '+', '*', '-' or ':'

def calculate_from_string(math_expression):
    """
    This function returns the calculation of a string got as an argument
    math_expression (str) is the expression the function need to calculate
    The function assumes that math_expression's format is: 
    number, space, string_without_spaces, space, another number
    The function calls 'calculate_mathematical_expression' in order to calculate the expression
    """
    expression_splited = math_expression.split(" ")
    # expression_splited is a list of 3 elements (by the assumption)
    # the first element is the first number, the second is the operation and the third is the second number
    # the elements of the list are str, so the function will convert them to number
    num1 = float(expression_splited[0]) 
    calc_type = expression_splited[1]
    num2 = float(expression_splited[2])
    return calculate_mathematical_expression(num1, num2, calc_type) 


