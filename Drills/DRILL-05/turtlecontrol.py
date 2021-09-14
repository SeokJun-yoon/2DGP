import turtle as t

# 재시작 함수
def restart():
    t.reset()
    t.stamp()

# 상단 이동 함수
def top_move():
    t.setheading(90)
    t.forward(50)
    t.stamp()

# 하단 이동 함수
def bottom_move():
    t.setheading(270)
    t.forward(50)
    t.stamp()

# 좌측 이동 함수
def left_move():
    t.setheading(180)
    t.forward(50)
    t.stamp()

# 우측 이동 함수
def right_move():
    t.setheading(0)
    t.forward(50)
    t.stamp()

t.stamp()
t.shape('turtle')
t.onkey(top_move,'w')
t.onkey(bottom_move,'s')
t.onkey(left_move,'a')
t.onkey(right_move,'d')
t.onkey(restart,'Escape')
t.listen()

