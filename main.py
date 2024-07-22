import colorgram
import turtle as t
import random

# def get_colors(image, num_color):
#     """return a color list extracted from the image"""
#     colors = colorgram.extract(image, num_color)
#     color_list = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb = (r,g,b)
#         color_list.append(rgb)
#
#     return color_list
#
#
# colors = get_colors('hirst.jpg', 33)
# print(colors)
# print(len(colors))


def fill_x(obj, num_dot):
    t.colormode(255)    # to enable rgb color
    for _ in range(num_dot):
        color = random.choice(color_list)
        obj.dot(20, color)
        obj.forward(50)


color_list = [(218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152), (162, 104, 151), (42, 47, 66), (128, 174, 115), (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78), (228, 189, 141), (194, 91, 72), (220, 226, 221), (62, 49, 38), (115, 41, 56), (91, 143, 118), (70, 67, 52), (209, 181, 189), (181, 185, 210), (209, 183, 178), (89, 55, 47), (183, 201, 179), (172, 199, 204), (41, 73, 83), (138, 130, 114), (47, 54, 50), (53, 70, 67)]

tim = t.Turtle()
tim.hideturtle()    # hide turtle
tim.penup()    # prevent drawing of line marks
tim.setposition(-200, -250)    # offset x,y home position
tim.speed("fastest")

y_axis = 0

while y_axis < 10:
    fill_x(tim, 10)
    tim.teleport(-200, tim.ycor() + 50)
    y_axis += 1


screen = t.Screen()
screen.exitonclick()
