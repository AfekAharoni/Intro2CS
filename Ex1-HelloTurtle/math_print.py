#################################################################
# FILE : math_print.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that prints calculates by math library
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: https://docs.python.org/3/library/math.html -> math functions in python
# NOTES: None
#################################################################
import math

def golden_ratio():
    """This function prints the golden ratio"""
    print((1+math.sqrt(5))/2)

def six_squared():
    """This function prints 6^2"""
    print(math.pow(6, 2))

def hypotenuse():
    """This function prints the hypotenuse of a triangle with 2 sides, one 12 and one 5"""
    print(math.sqrt(math.pow(12, 2) + math.pow(5, 2)))

def pi():
    """This function prints the pi value"""
    print(math.pi)

def e():
    """This function prints the e value"""
    print(math.e)

def squares_area():
    """This function prints all the areas of squares with sizes 1-1, 2-2, .... 10-10"""
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()