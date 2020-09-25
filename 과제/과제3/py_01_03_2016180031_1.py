import turtle # turtle use

def Move(x,y):  # 이동 함수
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def Nieun():    # 니은 그리기 함수
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(120)

# 'ㅇ' 
Move(-300,200)
turtle.circle(50)

# 'ㅡ' 
Move(-380,150)
turtle.forward(160)

#'ㅣ' 
Move(-325,150)
turtle.right(90)
turtle.forward(30)

# 'l' 
Move(-275,150)
turtle.forward(30)

# 니은 위치로 이동
Move(-340,100)

# 니은
Nieun()

# 'ㅅ' 오른쪽  
Move(-100,300)
turtle.right(120)
turtle.forward(130)

# 'ㅅ' 왼쪽
Move(-100,300)
turtle.left(60)
turtle.forward(130)

# 'ㅓ'
Move(-30,230)
turtle.left(60)
turtle.forward(40)
turtle.left(90)
turtle.forward(70)
turtle.left(180)
turtle.forward(130)

# 'ㄱ'
Move(-120,150)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# 'ㅈ' 위쪽
Move(70,300)
turtle.left(90)
turtle.forward(180)

# 'ㅈ' 왼쪽
Move(160,300)
turtle.right(120)
turtle.forward(120)

# 'ㅈ' 오른쪽
Move(160,300)
turtle.left(60)
turtle.forward(120)

# 'ㅡ'
Move(70,160)
turtle.left(60)
turtle.forward(180)

# 'ㅣ'
Move(150,160)
turtle.right(90)
turtle.forward(40)

# 니은 위치로 이동
Move(100,110)

# 니은
Nieun()

turtle.exitonclick()
