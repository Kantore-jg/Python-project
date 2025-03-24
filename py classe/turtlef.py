from turtle import *
import turtle
def triangle(color):
    turtle.color(color)
    for _ in range(3):
        turtle.forward(100) 
        turtle.left(120) 
        
        


screen = turtle.Screen()
colors = ["black", "green", "blue", "yellow", "purple"]


for i, color in enumerate(colors):
    turtle.penup()
    turtle.goto(-200 + i * 100, 0)  
    turtle.pendown()
    triangle(color)
    write("Kantore")
    

turtle.hideturtle()
screen.exitonclick()
