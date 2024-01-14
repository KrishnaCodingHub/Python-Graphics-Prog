import turtle
import time
import random
import winsound
screen = turtle.Screen()
# screen.setup(500, 500)
screen.bgcolor('blue')

kite = turtle.Turtle()
tur_kite=turtle.Turtle()
tur_thrd=turtle.Turtle()
tur_line=turtle.Turtle()
txt_ani=turtle.Turtle()
tur_kite.hideturtle()
tur_thrd.hideturtle()
tur_line.hideturtle()
txt_ani.hideturtle()
kite.hideturtle()
img=turtle.Turtle()

win = turtle.Screen()
win2 = turtle.Screen()
win3 = turtle.Screen()

win.setup(width=1.0, height=1.0, startx=None, starty=None)
kite.width(3)
colors = ['yellow','white','purple','orange','cyan','magenta','pink']

def draw_kite():
    kite.color("red")
    kite.fillcolor("yellow")
    kite.begin_fill()
    for side in range(4):
        kite.left(45)
        kite.forward(200)
        kite.left(45)
    kite.end_fill()

def draw_thred():
    tur_thrd.hideturtle()
    tur_thrd.pensize(2)
    tur_thrd.color("magenta")
    tur_thrd.speed(200)
    tur_thrd.penup()
    tur_thrd.setpos(-500, -150)
    tur_thrd.pendown()

    for thr in range(48):
        tur_thrd.right(330)
        tur_thrd.forward(10)
        tur_thrd.left(330)
        # tur_thrd.forward(10)

def draw_line():
    tur_line.color("red")
    tur_line.width(3)
    tur_line.begin_fill()
    tur_line.left(50)
    tur_line.penup()
    tur_line.setpos(-140,140)
    tur_line.pendown()
    tur_line.circle(-185,100)

def draw_kite_tail():
    tur_kite.hideturtle()
    tur_kite.width(3)
    tur_kite.begin_fill()
    tur_kite.color("red")
    tur_kite.left(52)
    tur_kite.backward(45)
    tur_kite.left(-52)
    tur_kite.forward(60)
    tur_kite.left(131)
    tur_kite.forward(49)
    tur_kite.end_fill()
    tur_kite.color("red")
    tur_kite.penup()
    tur_kite.setpos(0,0)
    tur_kite.pendown()
    tur_kite.left(-41)
    tur_kite.forward(280)

def kite_text():
    # number_of_characters = 1
    txt_kite = turtle.Turtle()

    txt_kite.hideturtle()
    txt_kite.penup()
    # txt_kiteine.setpos(-140, 140)
    txt_kite.setx(-85)
    txt_kite.sety(50)
    txt_kite.pendown()
    txt_kite.color("magenta")
    # msg="💖    💖"
    msg="★    ★"
    txt_kite.write(msg + '\n', font=("Verdana", 40, "bold"))

def animate_text(text):
    txt_ani.hideturtle()
    txt_ani.penup()
    txt_ani.setx(-350)
    txt_ani.sety(-250)
    txt_ani.pendown()

    while True:
        msg=random.choice(text)
        txt_ani.speed(20)
        txt_ani.write("\n")
        txt_ani.color(random.choice(colors))

        txt_ani.write(msg+'\n', font=("Verdana", 40, "bold"))
        time.sleep(1)
        txt_ani.clear()

def flyimag(x,y):
    img=turtle.Turtle()
    win.addshape("g4.gif")
    img.penup()
    # img.setx(x)
    # img.sety(y)
    img.goto(x,y)
    img.pendown()
    img.shape("g4.gif")
    # img.shape("smpp-2.gif")

def fly_bird(x,y):
    img=turtle.Turtle()
    win.addshape("smpp.gif")
    img.penup()
    # img.setx(x)
    # img.sety(y)
    img.goto(x,y)
    img.pendown()
    img.shape("smpp.gif")
    # img.shape("smpp-2.gif")

def fly_bird1(x,y):
    win2.addshape("smpp-2.gif")
    img.penup()
    img.goto(x,y)
    img.pendown()
    img.shape("smpp-2.gif")

def fly_bird2(x, y):
    img2=turtle.Turtle()
    win3.addshape("smpp-3.gif")
    img2.penup()
    img2.goto(x, y)
    img2.pendown()
    img2.shape("smpp-3.gif")

def animate_rocket(x,y):
    tur_sun=turtle.Turtle()
    for i in range(200):
        tur_sun.speed(200)
        tur_sun.goto(x, y)
        tur_sun.color("yellow")
        tur_sun.forward(80)
        tur_sun.left(3)

def draw_sun(x,y):
    t2=turtle.Turtle()
    t2.hideturtle()
    t2.speed(20)
    t2.color('red', 'yellow')
    t2.penup()
    # img.setx(x)
    # img.sety(y)
    t2.setposition(x, y)
    t2.pendown()
    t2.begin_fill()
    for i in range(36):
        t2.forward(150)
        t2.left(170)
    t2.end_fill()
    t2.hideturtle()

def play_music():
    winsound.PlaySound('flykite.wav', winsound.SND_ASYNC)

play_music()
draw_kite()
draw_line()
draw_kite_tail()
kite_text()
flyimag(-568,-200)
draw_thred()

fly_bird(140,280)
fly_bird1(320,180)
fly_bird2(400,300)

draw_sun(-568,200)

wishing_msgs = ["💖 Happy Makar Sankranti 💖",
                "💖 Happy Magh Bihu 💖",
                "💖 Happy Tila Sakraat 💖",
                "💖 Happy Makara Sankramana 💖",
                "💖 Happy Poush Sankranti 💖",
                "💖 Happy Pedda Panduga 💖",
                "💖 Happy Maghi Sankrant 💖",
                "💖 Happy Uttarayan 💖",
                "💖 Happy Sankranti 💖",
                "💖 Happy Lohri 💖",
                "💖 Happy Pongal 💖",
                "💖 Happy Makaravilakku 💖",
                "💖 Happy Sakrat 💖"]
# animate_text("💖 Happy\n       Makar\n          Sankranti 💖")
animate_text(wishing_msgs)

turtle.done()
# This code is contributed by Krishna Kushwaha
