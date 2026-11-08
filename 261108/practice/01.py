import turtle as t
import random

def draw_eyes(x, y):
    t.pencolor("black")
    colors = ["orange", "black", "white", "red", "blue", "brown", "purple", "green"]
    eye_color = random.choice(colors)
    t.fillcolor(eye_color)
    t.penup()
    t.setheading(random.randint(-50, 50))
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    eyes_size = random.randint(60, 100)
    t.circle(eyes_size)
    t.end_fill()
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.goto(x + eyes_size * 0.4, y + eyes_size * 0.8)
    t.pendown()
    t.begin_fill()
    t.circle(eyes_size - 50)
    t.end_fill()
    t.pencolor("brown")
    t.penup()
    t.setheading(120)
    t.goto(x + 50, y + 180)
    t.pendown()
    t.circle(60, 120)

# 基础设置
t.setup(800, 800)
t.bgcolor("white")
t.title("基础版圆形笑脸")
t.speed(0)
t.pensize(3)

# 画脸
t.pencolor("orange")
t.fillcolor("#FFD966")
t.penup()
t.goto(0, -250)
t.pendown()
t.begin_fill()
t.circle(250)
t.end_fill()

# 画左眼
draw_eyes(-85, 20)

# 画右眼
draw_eyes(105, 0)

# 画嘴巴
mouth_type = random.choice(["smile", "surprise", "tongue"])

if mouth_type == "smile":
    t.pencolor("brown")
    t.pensize(5)
    t.penup()
    t.goto(-130, -10)
    t.pendown()
    t.setheading(random.randint(-65, -55))
    t.circle(random.randint(120, 180), random.randint(100, 140))

elif mouth_type == "surprise":
    t.pencolor("brown")
    t.pensize(5)
    t.penup()
    sx = random.randint(-30, 30)
    sy = random.randint(-120, -60)
    sr = random.randint(15, 35)
    t.goto(sx, sy)
    t.pendown()
    t.fillcolor(random.choice(["red", "darkred", "pink"]))
    t.begin_fill()
    t.circle(sr)
    t.end_fill()

elif mouth_type == "tongue":
    t.pencolor("brown")
    t.pensize(5)
    t.penup()
    tx = random.randint(-140, -100)
    ty = random.randint(-30, 10)
    t.goto(tx, ty)
    t.pendown()
    t.setheading(random.randint(-70, -50))
    t.circle(random.randint(130, 170), random.randint(80, 110))
    t.setheading(random.randint(-100, -80))
    t.fillcolor(random.choice(["red", "darkred", "pink"]))
    t.begin_fill()
    t.circle(random.randint(12, 22))
    t.end_fill()

t.done()