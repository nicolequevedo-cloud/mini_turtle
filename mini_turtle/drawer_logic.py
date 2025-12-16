# mini_turtle/drawer_logic.py
import turtle

t = turtle.Turtle()
t.speed(1)

posicion_x = 0

def adelante(pasos):
    global posicion_x
    t.forward(pasos)
    posicion_x += pasos

def abajo(pasos):
    global posicion_x
    t.right(90)
    t.forward(pasos)
    t.left(90)

def reiniciar():
    global posicion_x
    t.penup()
    t.home()
    t.pendown()
    posicion_x = 0
