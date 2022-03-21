import turtle
t=turtle.Turtle()
t.width(20)      #펜 굵기 20

t.shape("turtle")
t.color("cyan")   #거북이 색을 바꾼뒤 원을그리고 up으로 펜을올려서 이동 흔적이 표시 안되게한다
t.circle(100)
t.up()

t.color("black")
t.forward(180)
t.down()         #펜을 다시 내려서 커서의 이동을 표시하게한다
t.circle(100)
t.up()

t.color("red")
t.forward(180)
t.down()
t.circle(100)

t.color("green")
t.left(120)
t.up()
t.forward(50)
t.down()
t.left(60)
t.up()
t.forward(50)
t.down()
t.circle(100)
t.up()

t.color("yellow")
t.forward(200)
t.down()
t.circle(100)