# import colorgram
#
# # 10 objects are returned
# colors = colorgram.extract('myImage.jpg', 30)
#
# color_palette = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r, g, b))
#
# print(color_palette)

import turtle, random

turtle.colormode(255)

tim = turtle.Turtle()
tim.speed("fastest")
color_list = [
    (243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166),
    (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81),
    (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96),
    (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188)]

# for _ in range(10):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#

x = 0
y = 0
for j in range(10):
    tim.setx(x)
    tim.sety(y)
    for i in range(10):
        c = random.choice(color_list)
        tim.color(c)
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        x += 30
        tim.setx(x)
    x = 0
    y += 30

screen = turtle.Screen()
screen.exitonclick()
