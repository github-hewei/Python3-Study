# 海龟绘图模块
import turtle

# 定义画笔的样式
pen_style = {
    'speed': 1,         # 速度
    'pencolor':'red',  # 颜色
    'pensize': 4        # 大小
}

# 设置画笔的样式
turtle.pen(**pen_style)

# 往上移动200
turtle.penup()
turtle.goto(0,200)

# 填充
turtle.begin_fill()
turtle.color("red")

# 画笔落下，一顿乱画
turtle.pendown()
turtle.goto(-10,220)
turtle.left(120)
turtle.circle(80, 120)
turtle.circle(120, 60)
turtle.circle(140, 40)
turtle.goto(-64,32)
turtle.goto(0,0)
turtle.goto(64,32)
turtle.left(40)
turtle.circle(140, 40)
turtle.circle(120,60)
turtle.circle(80,122)

# 填充结束
turtle.end_fill()

# 画笔抬起
turtle.penup()

# 移动到中心写字
turtle.goto(-40,120)

turtle.color("yellow")
turtle.write("梅梅 I LOVE U",)
turtle.penup()

turtle.hideturtle()
turtle.done()