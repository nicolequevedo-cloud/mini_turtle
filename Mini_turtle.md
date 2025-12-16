# mini_turtle

Codigo:

```
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

#ESCALERA -
t = turtle.Turtle()
t.speed(2)

posicion_x = 0

def adelante(distancia):
    global posicion_x
    t.forward(distancia)
    posicion_x += distancia

def abajo(distancia):
    t.right(90)
    t.forward(distancia)
    t.left(90)

def dibujar_escalera():
    for _ in range(3):
        adelante(90)
        abajo(60)

dibujar_escalera()

# BORRAR SOLO LA ESCALERA
t.clear()
t.hideturtle()

#Corazon 
pen = turtle.Turtle()
pen.speed(3)
pen.color("black", "white")

# MUY IMPORTANTE
pen.penup()
pen.goto(-50, -50)   # posición visible
pen.setheading(0)    # dirección correcta
pen.pendown()

pen.begin_fill()
pen.left(140)
pen.forward(113)

for _ in range(200):
    pen.right(1)
    pen.forward(1)

pen.left(120)

for _ in range(200):
    pen.right(1)
    pen.forward(1)

pen.forward(112)
pen.end_fill()

turtle.done()
