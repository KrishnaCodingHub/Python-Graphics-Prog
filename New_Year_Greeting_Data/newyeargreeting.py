import datetime as dt
import turtle
import time
import random
import winsound

turtle.hideturtle()
# create a turtle to display time
t = turtle.Turtle()


# create a turtle to create rectangle box
trl_rect = turtle.Turtle()
trl_sky_star = turtle.Turtle()
trl_firework =turtle.Turtle()
trl_countdwon =turtle.Turtle()
text = turtle.Turtle()

# create screen
newyear_win= turtle.Screen()
win=turtle.Screen()
trl_rect.hideturtle()
trl_sky_star.hideturtle()
trl_firework.hideturtle()
t.hideturtle()
text.hideturtle()
trl_countdwon.hideturtle()
newyear_win.setup(width=1.0, height=1.0, startx=None, starty=None)
 #remove close,minimaze,maximaze buttons:
# canvas = newyear_win.getcanvas()
# root = canvas.winfo_toplevel()
# root.overrideredirect(1)
newyear_win.bgcolor("black")
colors=['medium blue','blue violet','yellow','green','white','blue','purple','orange','cyan'
		,'red','magenta','goldenrod']
def play_fireworkmusic():
	winsound.PlaySound('animalsong.wav', winsound.SND_ASYNC)
def play_countdown_music():
	winsound.PlaySound('mixkit-female-countdown.wav', winsound.SND_ASYNC)
def old_year_txt():
	# Move turtle to air
	trl_countdwon.up()

	# Move turtle to a given position
	# trl_countdwon.setpos(-68, 95)

	# Move the turtle to the ground
	trl_countdwon.down()
	# text.hideturtle()
	text.color("green yellow")
	text.penup()
	text.sety(250)
	text.write("💖´ *•.¸♥¸.•** 𝒢❁❁𝒹 𝐵𝓎𝑒 𝟤💗𝟤𝟥 **•.¸♥¸.•*´💖", font=("None", 40, "bold"), align="center")
	# text.write("💖🍬  🎀  𝒢❁❁𝒹 𝐵𝓎𝑒 𝟤💗𝟤𝟥  🎀  🍬💖", font=("None", 30, "bold"), align="center")



def countdown():
	win.addshape('countdown_img.gif')
	win.title("New Year Greeting Card")
	img=turtle.Turtle()
	# win.bgcolor('black')
	img.shape('countdown_img.gif')
	old_year_txt()

	countdown=10
	# trl_countdwon.hideturtle()
	trl_countdwon.goto(0, -70)
	trl_countdwon.color("magenta")
	# Play countdown music
	play_countdown_music()

	for timer in range(countdown,-1,-1):
		trl_countdwon.write(timer,align='center',font=("Agency FB", 80, "bold"))
		time.sleep(1)
		trl_countdwon.clear()
	trl_rect.clear()
	img.clear()
	win.clear()
	text.clear()

# create cound screen
countdown()
# set background color of the screen




# newyear_win.bgcolor("black")

# obtain current hour, minute and second
# from the system
formatted_date = dt.date.today().strftime('%d %b %Y')

trl_rect.pensize(1)
# t1.color('blue')
trl_rect.penup()

# Draw firework
def draw_firework(trt_obj, size):
	# trt_obj.color("red", "yellow")
	trt_obj.color(random.choice(colors),random.choice(colors))
	trt_obj.speed(300)
	for _ in range(36):
		# trt_obj.color(random.choice(colors))
		trt_obj.forward(size)
		trt_obj.left(170)

def draw_star(trt_obj, size):

	# trt_obj.color("white", "yellow")
	trt_obj.color(random.choice(colors))
	trt_obj.speed(500)
	for _ in range(6):
		trt_obj.forward(size)
		trt_obj.left(216)


# Creating a turtle object(pen)
pen = turtle.Turtle()
pen.hideturtle()

# Defining a method to draw curve
def curve():
	pen.speed(500)
	pen.pensize(5)
	for i in range(200):
		pen.color("red")
		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)


# Defining method to draw a full heart
def heart():
	pen.speed(500)
	pen.pensize(5)
	pen.color("red")
	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()


# Defining method to write text
def txt():
	win.addshape('ganesh2.gif')
	img = turtle.Turtle()
	# win.bgcolor('black')
	img.setpos(-590,300)
	img.shape('ganesh2.gif')
	img.setpos(0, 300)
	img.shape('ganesh2.gif')
	# text.hideturtle()
	text.color("orange")
	text.penup()
	text.sety(200)
	text.write("🐹 🎀 💖 Happy New Year 2024 💖 🎀 🐹", font=("Trattatello", 40, "bold"), align="center")




def animate_text(text):
	number_of_characters = 1
	txt_ani = turtle.Turtle()
	txt_ani.hideturtle()
	txt_ani.setx(-90)
	txt_ani.sety(20)
	while True:
		txt_ani.speed(500)
		# txt_ani.goto(-100, 2)
		# pen.setpos(-100, -10)

		txt_ani.write("\n")
		txt_ani.color("floral white")
		# txt_ani.write("💖 Happy\n       New Year\n          2024 💖", font=("Verdana", 15, "bold"))
		txt_ani.write(text+'\n', font=("Verdana", 15, "bold"))

		# txt_ani.write(text[0:number_of_characters], font=("None", 10,))
		# number_of_characters += 1
		# if number_of_characters > len(text):
		# 	number_of_characters = 0
		time.sleep(0.3)
		txt_ani.clear()


newyear_win.bgcolor('black')
# play firework music
play_fireworkmusic()
# # Write text
txt()
#  Draw sky stars
for _ in range(100):
	x,y =random.randint(-700,700), random.randint(-700,700)
	trl_sky_star.penup()
	trl_sky_star.goto(x,y)
	trl_sky_star.pendown()
	trl_sky_star.begin_fill()
	draw_star(trl_sky_star,random.randint(5,25))
	trl_sky_star.end_fill()


# Draw firework
for _ in range(25):
	# x,y =random.randint(-600,200), random.randint(-600,200)
	x, y = random.randint(-680, 680), random.randint(-190, 190)
	trl_firework.penup()
	trl_firework.goto(x,y)
	trl_firework.pendown()
	trl_firework.begin_fill()
	draw_firework(trl_firework,random.randint(50,100))
	trl_firework.end_fill()
	# trl_firework.hideturtle()






# # To hide turtle
# pen.ht()
pen.setpos(0, -20)
# Draw a heart
heart()



# Main Program Starts Here....
animate_text("💖 Happy\n       New Year\n          2024 💖")
newyear_win.exitonclick()


