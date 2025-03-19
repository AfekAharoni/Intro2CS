#################################################################
# FILE : hello_turtle.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that draw fleet with turtle library
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################
import turtle

def draw_triangle():
    """This function draw triangle with turtle library"""
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)

def draw_sail():
    """This function draw sail with turtle library"""
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)

def draw_ship():
    """This function draw ship with turtle library"""
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(30)

def draw_fleet():
    """This function draw 2 ships, by distance of 300 steps"""
    draw_ship()
    turtle.left(90)
    turtle.forward(300)
    turtle.right(180)
    draw_ship()
    turtle.right(90)
    turtle.forward(300)

if __name__ == "__main__" :
    draw_fleet()
    turtle.done()
