import random
import turtle
from turtle import mainloop, hideturtle


# 画心
def draw_heart(size, color_):
    turtle.speed(0)
    turtle.colormode(255)
    turtle.color(color_)
    turtle.pensize(2)
    turtle.pendown()
    turtle.setheading(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size * -3.745, 45)
    turtle.circle(size * -1.431, 165)
    turtle.left(120)
    turtle.circle(size * -1.431, 165)
    turtle.circle(size * -3.745, 45)
    turtle.fd(size)
    turtle.end_fill()


# 随机颜色，大小，位置
def draw():
	# 随机颜色
    colors1 = random.randint(0, 255)
    colors2 = random.randint(0, 255)
    colors3 = random.randint(0, 255)
    turtle.penup()
    # 随机位置
    x = random.randint(-400, 400)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    # 随机大小
    size = random.randint(10, 20)
    draw_heart(size, (colors1, colors2, colors3))


# 主函数
def main():
    hideturtle()
    turtle.setup(900, 500)
    # 更改心出现的个数
    for i in range(30):
        draw()
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.color(0,0,0)
    turtle.write('XXXXXXXXXXX', font=('宋体', 60, 'bold'))
    mainloop()


main()
