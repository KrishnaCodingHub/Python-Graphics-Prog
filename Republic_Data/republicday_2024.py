import turtle
tur_main=turtle.Turtle()
win=turtle.Screen()
tur_main.hideturtle()



win.setup(width=1.0, height=1.0, startx=None, starty=None)
win.bgcolor("blue")
def back_ground():
    tur_main.write("Republic Day 2024")

def create_stand():
    tur_stand = turtle.Turtle()
    tur_stand.color("white")
    tur_stand.pensize(5)
    tur_stand.left(90)
    tur_stand.forward(400)

    # tur_stand.forward(4)
    # tur_stand.begin_fill()

    tur_stand.penup()
    tur_stand.setposition(-100,280)
    tur_stand.pendown()

    tur_stand.goto(-100, 280)


    # tur_stand.end_fill()

# creating flag turtle object
tur_flag = turtle.Turtle()
tur_flag.hideturtle()
tur_flag.penup()
tur_flag.setposition(-100,80)
tur_flag.pendown()
def create_flag( color):
    tur_flag.color(color)
    tur_flag.begin_fill()

    tur_flag.forward(400)
    tur_flag.left(90)
    tur_flag.forward(80)
    tur_flag.left(90)
    tur_flag.forward(400)
    tur_flag.left(180)
    # tur_flag.forward(50)
    # tur_flag.left(90)
    tur_flag.end_fill()



# create Back Ground screen
back_ground()
# create_stand()
# create flag
# create_flag("green")
# create_flag("white")
# create_flag("orange")
create_stand()
win.exitonclick()