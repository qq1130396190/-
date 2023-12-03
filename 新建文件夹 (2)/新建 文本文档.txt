import turtle
# 初始化海龟对象
t = turtle.Turtle()
# 定义蛇头移动函数
def move():
    global x, y, dir
    x += dir
    y += dir

    # 判断蛇头的位置是否超出屏幕范围
    if x < 0 or x > width or y < 0 or y > height:
        dir *= -1

    # 如果蛇头碰到了墙或者身体，则重新设定方向
    if abs(x - lastX) <= radius + 50 and abs(y - lastY) <= radius + 50:
        dir = random(-1, 1)
        lastX = x
        lastY = y

    # 画出蛇身和