import turtle

count=0

x=-250
y=250
while (count<6):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    y=y-100
    count=count+1

turtle.penup()
turtle.goto(x,y)
turtle.right(90)
y=250
count=0

while (count<6):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    x=x+100
    count=count+1
    
turtle.exitonclick()
    
    
