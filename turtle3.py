import turtle
s=turtle.Turtle()
turtle.title("rinta's turtle program")
turtle.bgcolor("lavender")
s.shapesize(1,5,10)
s.pencolor("white")
for i in range(5):
    s.forward(150)
    s.right(144)
s.fillcolor("black")
s.begin_fill()
s.circle(60)
s.end_fill()
s.dot(20)
