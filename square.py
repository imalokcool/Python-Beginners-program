import turtle
n = int(input("number of sides:"))
list = ["red","green","blue","yellow"]
paper = turtle.Screen()
pen = turtle.Turtle()
for i in range(0,n):
    pen.color(list[i])
    pen.fillcolor("black")
    pen.forward(50)
    pen.right(360/n)