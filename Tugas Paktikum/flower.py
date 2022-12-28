import turtle

turtle.bgcolor('black')
turtle.speed(100)
turtle.hideturtle()

colors = ["red","blue","red","blue"]

for i in range(150):
    for c in colors:
        turtle.color(c)
        turtle.circle(500-i,100)
        turtle.lt(80)
        turtle.circle(500-i,100)
        turtle.end_fill()

turle.mainloop()