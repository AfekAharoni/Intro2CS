#################################################################
# FILE : shapes.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex2 2025
# DESCRIPTION: In this file there are 4 functions that calculate area of different shapes
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################
import math

def shape_area():
    """
    This function gets a shape as an input from the user, and calculate the area of it
    The function uses other functions:
    circle_area = when the user choose the shape circle
    rectangle_area = when the user choose the shape rectangle
    triangle_area = when the user choose the shape triangle
    """
    shape = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape != 1 and shape != 2 and shape != 3: # if the user didn't enter 1,2 or 3
        return None
    if shape == 1: # the user choose circle
        area = circle_area()
    elif shape == 2: # the user choose rectangle
        area = rectangle_area() 
    else: # if the function got here, the user choose triangle
        area = triangle_area()
    return area # returns the area by the shape

def circle_area():
    """
    This function returns the area of a circle, by the radius
    This function uses the math library:
    math.pi -> PI value
    math.pow(x,y) -> x^y
    The formula is: PI * radius ^ 2
    The function assumes that the radius is bigger than zero
    """
    radius = float(input()) # get radius as input
    return math.pi * (math.pow(radius, 2))

def rectangle_area():
    """
    This function returns the area of a rectangle, by the sides got
    first_side and second_side are numbers
    The formula is: first_side * second_side
    The function assumes that the sides are bigger than zero
    """
    first_side = float(input()) # get first side as input 
    second_side = float(input()) # get second side as input
    return first_side * second_side

def triangle_area():
    """
    This function returns the area of an equilateral triangle, by the side got
    side is a number 
    This function uses the math library:
    math.sqrt(x) -> the root of x
    math.pow(x,y) -> x^y
    The formula is: (side^2 / 4 ) * root of 3
    The function assumes that the side is bigger than zero
    """
    side = float(input()) # get the side as input
    return (math.sqrt(3) / 4 ) * math.pow(side, 2)

