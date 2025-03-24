import turtle as t
import random
tin=t.Turtle()
colours=['red','green','blue','yellow','black']
directions=[0,90,180,270]
tin.pensize(20)
tin.speed('fastest')
tin.circle(100)
for _ in range(200):
    tin.forward(30)
    tin.setheading(random.choice(directions))
    tin.color(random.choice(colours))

screen= t.Screen()
screen.exitonclick()
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range (num_sides):
#         tin.forward(100)
#         tin.right(angle)
# for i in range (3,11):
#     tin.color(random.choice(colours))
#     draw_shape(i)