import turtle
import random

def screenLeftClick(x, y):       #왼쪽버튼누르면 스탬프찍는 함수
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 8)  #랜덤크기 1부터 7까지

    tAngle = random.randrange(0, 360) #각도0부터 360도까지

    turtle.shapesize(tSize)  #색상,크기,각도
    turtle.color(r, g, b)
    turtle.right(tAngle)

    turtle.stamp()        #커서를 화면에 찍게함

    turtle.penup()        #펜을 올려서 커서이동 흔적 안되게하기
    turtle.goto(x, y)     #지정좌표 (x,y)로 이동시키기

r, g, b = 0.0, 0.0, 0.0   #변수 초기값

turtle.shape("turtle")
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()