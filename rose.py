import turtle

# Set up the turtle screen
t = turtle.Turtle()
turtle.bgcolor("white")
t.speed(100)

# Function to draw a curve (used to make the petals)
def draw_curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

# Function to draw the rose
def draw_rose():
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(100)
    draw_curve()
    t.left(120)
    draw_curve()
    t.forward(100)
    t.end_fill()

# Function to draw the stem
def draw_stem():
    t.color("green")
    t.right(150)
    t.forward(200)

# Function to draw leaves
def draw_leaf():
    t.begin_fill()
    t.left(45)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(135)
    t.forward(70)
    t.end_fill()

# Drawing the rose and stem
draw_rose()
draw_stem()

# Drawing the leaves
t.right(90)
t.forward(100)
draw_leaf()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
