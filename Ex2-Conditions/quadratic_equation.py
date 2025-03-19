#################################################################
# FILE : quadratic_equation.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex2 2025
# DESCRIPTION: In this file there are 2 functions that calculate quadratic equation result by input from the user
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################
import math

def quadratic_equation(a, b, c):
    """
    This function calculate the result of quadratic equation
    The function gets three arguments:
    a, b, c - numbers
    The quadratic equation is ax^2 + bx + c = 0
    The function assumes that a is not 0
    The function returns two results, because the equation has maximum 2 results
    If there is no result for the equation, the function returns None, None
    If there is one result only for the equation, the function returns one result and None
    If there is two results, the function returns them both
    The function uses math library: 
    math.pow(x, y) = x^y
    math.sqrt(x) = the root of x
    The function assumes that the arguments are valid
    """
    discriminant = math.pow(b, 2) - 4 * a * c # the discriminant is the inside number of the root
    if discriminant < 0: # if the discriminant is lower than zero, there is no solutions
        return None, None
    first_res = (-b + math.sqrt(discriminant)) / (2 * a)
    second_res = (-b - math.sqrt(discriminant)) / (2 * a)
    if discriminant == 0: # if the discriminant is zero, first_res and second_res will be the same
        return first_res, None # could be: return second_res, None -> because first_res = second_res
    # if the function got here, the discriminant is higher than zero and there is 2 results
    return first_res, second_res # could be: return second_res, first_res -> the order isn't necessary

def quadratic_equation_user_input():
    """
    This function gets input from the user -> a, b and c seperated with space between them
    The function splits the input it gots by the spaces and convert them to float
    The function prints the solutions for the quadratic equation, if there is any
    The function uses the function quadratic_equation
    """
    coeficcients = input("Insert coefficients a, b, and c: ") # gets input from the user
    coeficcients = coeficcients.split(" ") # split the text by spaces into a list
    a = float(coeficcients[0]) # convert the text to a number into 'a'
    b = float(coeficcients[1]) # convert the text to a number into 'b'
    c = float(coeficcients[2]) # convert the text to number into 'c'
    if a == 0: # if 'a' is zero, the equation is not a quadratic equation
        print("The parameter 'a' may not equal 0")
    else: # 'a' is not zero
        first_res, second_res = quadratic_equation(a, b, c) # use the function to get the results
        if first_res is None and second_res is None: # if there is no solutions
            print("The equation has no solutions")
        elif second_res is None: # if there is only one solution
            print("The equation has 1 solution: " + str(first_res))
        else: # if the function got here, there are 2 solutions for the equation
            print("The equation has 2 solutions: " + str(first_res) + " and " + str(second_res))

