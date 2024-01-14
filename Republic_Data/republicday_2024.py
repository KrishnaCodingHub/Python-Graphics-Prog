import turtle
tur_main=turtle.Turtle()
win=turtle.Screen()
tur_main.hideturtle()



win.setup(width=1.0, height=1.0, startx=None, starty=None)
win.bgcolor("blue")
def back_ground():
    tur_main.hideturtle()
    tur_main.write("Republic Day 2024")

def create_stand():
    tur_stand.color("white")
    tur_stand.pensize(10)
    # tur_stand.left(90)
    # tur_stand.forward(568)
    tur_stand.penup()
    tur_stand.setposition(-105, -250)
    tur_stand.left(90)
    tur_stand.forward(568)
    tur_stand.setposition(-105, -250)
    tur_stand.color("orange")
    tur_stand.shape("circle")
    # tur_stand.sety(-250)
    # tur_stand.setx(-105)

    # tur_stand.goto(-105, -250)

    tur_stand.pendown()
    # tur_stand.goto(0, -300)
    tur_stand.goto(-105, -250)

    # tur_stand.end_fill()
tur_stand = turtle.Turtle()
tur_stand.hideturtle()
# tur_stand.setposition(-105, -250)
# creating flag turtle object
tur_flag = turtle.Turtle()
tur_flag.hideturtle()
tur_flag.penup()
tur_flag.setposition(-101,80)
tur_flag.pendown()
tur_flag_wheel= turtle.Turtle()
tur_flag_wheel.hideturtle()
tur_flag_spoke= turtle.Turtle()
tur_flag_spoke.hideturtle()

def create_flag( color):
    tur_flag.color(color)
    tur_flag.begin_fill()

    tur_flag.forward(380)
    tur_flag.left(90)
    tur_flag.forward(70)
    tur_flag.left(90)
    tur_flag.forward(380)
    tur_flag.left(180)
    # tur_flag.forward(50)
    # tur_flag.left(90)
    tur_flag.end_fill()

# def flag_spoke():
#     # tur_flag_spoke.setposition(95,150)
#     tur_flag_spoke.setposition(100,200)
#     tur_flag_spoke.color("navy blue")
#     # tur_flag_spoke.shape("circle")
#     for _ in range(360):
#         # tur_flag_spoke.forward(3.5)
#         tur_flag_spoke.left(5)
def flag_spoke():

    for _ in range(24):

        tur_flag_spoke.speed(200)
        # tur_flag_spoke.goto(x, y)
        tur_flag_spoke.penup()
        tur_flag_spoke.setposition(96, 200)
        tur_flag_spoke.pendown()
        tur_flag_spoke.color("navy blue")
        tur_flag_spoke.forward(40)
        tur_flag_spoke.left(15)
def flag_wheel():
    # tur_flag_spoke.setposition(95,150)
    tur_flag_wheel.color("navy blue")
    tur_flag_wheel.penup()
    tur_flag_wheel.setposition(98,160)
    tur_flag_wheel.pendown()
    # tur_flag_spoke.shape("circle")
    for _ in range(90):
        tur_flag_wheel.left(5)
        tur_flag_wheel.forward(3.5)

    # tur_flag_wheel.goto(98, 160)

# create Back Ground screen
# back_ground()
create_stand()
# create flag
create_flag("green")
create_flag("white")
create_flag("orange")
flag_wheel()
# draw_circle()
flag_spoke()
# win.exitonclick()
turtle.done()