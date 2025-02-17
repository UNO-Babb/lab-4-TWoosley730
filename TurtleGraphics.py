#TurtleGraphics.py
#Name: Trevor Woosley
#Date: 02/16/2025
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(spongebob, sides):
    for s in range(sides):
        spongebob.forward(50)
        spongebob.right(365/sides)

def fillCorner(patrick, corner):
    drawSquare(patrick, 100)
    
    if corner == 1:
        patrick.begin_fill()
        drawSquare(patrick, 50)
        patrick.end_fill()
    
    elif corner == 2:
        patrick.forward(50)
        patrick.begin_fill()
        drawSquare(patrick, 50)
        patrick.end_fill()
    
def squaresInSquares(turtle, size, number):
    for i in range(10):
    draw_square(squidward, size)
    squidward.penup()
    squidward.forward(decrement) 
    squidward.right(90)  
    squidward.pendown()
    size -= decrement

def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 35)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
