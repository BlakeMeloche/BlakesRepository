#-------------------------------------------------------------------------------
# Name:        4.9.2
# Purpose: Squares in squares
#
# Author:      Blake Meloche
#
# Created:     09/18/2025
# Copyright:   (c) Blake Meloche 2025
# Licence:     <your licence>
#
#
#Note: I made it adjustable with a basic formula that should generally work so
#      you can select turtle used, side length(r), and number of squares(t)
#-------------------------------------------------------------------------------

import turtle
kurt = turtle.Turtle()

def drawSquare(turt, r, t):
    perimeter1 = r*8
    for j in range(t):
        r= r / 1.3
        turt.penup()
        turt.right(45)
        turt.forward(r/20)
        turt.left(45)
        turt.pendown()
        for f in range(4):
            turt.forward(r/4)
            turt.right(90)




drawSquare(kurt, 800, 5)
