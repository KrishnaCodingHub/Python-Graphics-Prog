import turtle
# tur_main=turtle.Turtle()
win=turtle.Screen()
def create_stand():
    tur_stand.color("blue")
    tur_stand.pensize(7)
    # tur_stand.left(90)
    # tur_stand.forward(568)
    tur_stand.penup()
    tur_stand.setposition(-105, -250)
    tur_stand.left(90)
    tur_stand.forward(568)
    # tur_stand.sety(-250)
    # tur_stand.setx(-105)

    # tur_stand.goto(-105, -250)

    tur_stand.pendown()
    # tur_stand.goto(0, -300)
    tur_stand.goto(-105, -250)

    # tur_stand.end_fill()
tur_stand = turtle.Turtle()
tur_stand.hideturtle()
create_stand()
turtle.done()