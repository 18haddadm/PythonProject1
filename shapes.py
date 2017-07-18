from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
for i in range(4):
    t.forward(50)
    t.left(90)

t.speed(0)

for i in range(52):
    t.forward(100)
    t.left(175)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.left(90)

# Close window on click.
