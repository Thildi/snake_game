from turtle import Turtle

for _ in range(30):

    def gestrichelte_linie(length, dashes, gap):
        for _ in range(dashes):
            turtle.forward(length)
            turtle.penup()
            turtle.forward(gap)
            turtle.pendown()


    gestrichelte_linie(100, 50, 20)
