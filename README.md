# mini_turtle

Codigo:
'''python  
import turtle

# ESCALERA
t = turtle.Turtle()
t.speed (1)
t.forward(90)
t.right(90)
t.forward(60)

t.left(90)
t.forward(90)

t.right(90)
t.forward(60)

t.left(90)
t.forward(90)

t.right(90)
t.forward(60)


t.reset()
t.speed(1)

#  CORAZÓN
pen = turtle.Turtle()
pen.speed (1)
pen.pencolor("black")
pen.fillcolor("white")

pen.begin_fill()
pen.left(140)
pen.forward(113)

for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.left(120)

for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.forward(112)
pen.end_fill()
'''



turtle.done()
