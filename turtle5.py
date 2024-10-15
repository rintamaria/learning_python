import turtle
t=turtle.Turtle()

def flower():
    for i in range(5):
        t.circle(190-i,90)
        t.left(90)
        t.circle(190-i,90)
        t.left(18)
flower()
