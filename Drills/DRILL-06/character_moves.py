from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 사각 운동
#def rect_move(x,y):
    

# 원 운동
#def circle_move(x,y):

# direction=1 -> 오른쪽
# direction=2 -> 위쪽
# direction=3 -> 왼쪽
# direction=4 -> 아래쪽
direction=1
x=400
y=90
degree=0

# 도형 타입 판별
shape_type=1    # 1 : 사각형 움직임, 2 : 원 움직임

while 1:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    if shape_type==1:
        if direction==1:
            x+=2
            if x>390 and x<400:
                shape_type=2    
            if x>780:
                x=780
                direction=2
        if direction==2:
            y+=2
            if y>560:
                y=560
                direction=3
        if direction==3:
            x-=2
            if x<20:
                x=20
                direction=4
        if direction==4:
            y-=2
            if y<90:
                y=90
                direction=1

    elif shape_type==2:
        x+=math.cos(degree/360*2*math.pi)*5
        y+=math.sin(degree/360*2*math.pi)*4
        degree+=1
        if degree>359:
            print(degree)
            x=400
            shape_type=1
            degree=0

delay(5)
    
close_canvas()
