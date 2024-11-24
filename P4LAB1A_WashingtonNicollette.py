#Nicollette Washington
#10/31/2024
#P4Lab1a
# Create a program that draws a trinagle and a square using turtle.

import turtle


tur = turtle.Turtle()

# Draw Elsa's triangle
tur.color("blue")
for _ in range(3):
    tur.forward(100)
    tur.left(120)

# Move to new position
tur.penup()
tur.goto(150, 0)
tur.pendown()

# Draw Anna's square
tur.color("pink")
for _ in range(4):
    tur.forward(100)
    tur.left(90)

# Keep window open
turtle.done()      
