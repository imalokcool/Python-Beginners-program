import turtle
paper = turtle.Screen()
pen = turtle.Turtle()
pen.fillcolor('blue')
pen.begin_fill()
for i in range(1):
    pen.circle(100)
pen.end_fill()
turtle.done()
