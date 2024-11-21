import turtle

screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Star using turtle")

t=turtle.Turtle()
t.pencolor("White")
t.pensize(5)
t.shape("arrow")
t.speed(5)
t.fillcolor("white")

t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill

t.left(90)
t.penup()
t.forward(50)
t.right(90)
t.pendown()

t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.right(120)
t.end_fill

t.hideturtle()
turtle.done()

