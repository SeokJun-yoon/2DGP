Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> turtle
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    turtle
NameError: name 'turtle' is not defined
>>> import turtle
>>> turtle
<module 'turtle' from 'C:\\Users\\kings\\AppData\\Local\\Programs\\Python\\Python38\\lib\\turtle.py'>
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.shape('turtle')
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(30)
>>> turtle.forward(100)
>>> turtle.left(120)
>>> turtle.forward(100)
>>> turtle.left(30)
>>> turtle.forward(100)
>>> turtle.forward(30)
>>> turtle.penup()
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.pendown()
>>> turtle.forward(80)
>>> turtle.reset()
>>> for i in range(4):
	turtle.forward(100)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(3):
	turtle.forward(100)
	turtle.left(120)

	
>>> turtle.reset()
>>> for i in range(5):
	turtle.forward(100)
	turtle.left(72)

	
>>> turtle.reset()
>>> for i in range(5):
	turtle.forward(100)
	turtle.left(144)

	
>>> turtle.reset()
>>> for i in range(90):
	turtle.forward(300)
	turtle.left(177)

	
Traceback (most recent call last):
  File "<pyshell#44>", line 3, in <module>
    turtle.left(177)
  File "<string>", line 8, in left
  File "C:\Users\kings\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1699, in left
    self._rotate(angle)
  File "C:\Users\kings\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Users\kings\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Users\kings\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Users\kings\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 799, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(60):
	turtle.forward(300)
	turtle.left(177)

	
>>> turtle.reset()
>>> for i in range(10):
	turtle.forward(300)
	turtle.left(89)

	
>>> turtle.speed(0)
>>> for i in range(10):
	turtle.forward(300)
	turtle.left(89)

	
>>> amount=300
>>> for i in range(100):
	turtle.forward(amount)
	turtle.left(89)
	amount-=2

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(100):
	turtle.forward(amount)
	turtle.left(89)
	amount-=2

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> amount=10
>>> for i in range(200):
	turtle.forward(amount)
	turtle.left(89)
	amount+=2

	

>>> turtle.reset()
>>> turtle.speed(0)
>>> turtle.reset()
>>> turtle.circle(200)
>>> turtle.right(90)
>>> turtle.circle(100)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    urtle.circle(100)
NameError: name 'urtle' is not defined
>>> turtle.circle(100)
>>> turtle.undo()
>>> turtle.goto(100,100)
>>> turtle.goto(200,-100)
>>> 
= RESTART: C:/Users/kings/OneDrive/바탕 화면/2020 2학기 수업/2D 게임프로그래밍/수업코드/9월_7일_수업_3.py
>>> 
= RESTART: C:/Users/kings/OneDrive/바탕 화면/2020 2학기 수업/2D 게임프로그래밍/수업코드/9월_7일_수업_3.py
>>> 
= RESTART: C:/Users/kings/OneDrive/바탕 화면/2020 2학기 수업/2D 게임프로그래밍/수업코드/9월_7일_수업_3.py
>>> 
= RESTART: C:/Users/kings/OneDrive/바탕 화면/2020 2학기 수업/2D 게임프로그래밍/수업코드/9월_7일_수업_3.py
>>> random
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    random
NameError: name 'random' is not defined
>>> import random
>>> random
<module 'random' from 'C:\\Users\\kings\\AppData\\Local\\Programs\\Python\\Python38\\lib\\random.py'>
>>> random.randint(1,6)
5
>>> random.randint(1,6)
2
>>> random.randint(1,6)
1
>>> random.randint(1,6)
4
>>> random.randint(1,6)
3
>>> random.randint(1,6)
6
>>> random.randint(1,6)
4
>>> random.randint(1,6)
3
>>> random.randint(1,6)
1
>>> random.randrange(1,6)
5
>>> random.randrange(1,6)
4
>>> random.randrange(1,6)
1
>>> random.randrange(1,6)
3
>>> random.randrange(1,6)
4
>>> random.randrange(1,6)
1
>>> random.randrange(1,6)
4
>>> random.randrange(1,6)
2
>>> random.randrange(1,6)
3
>>> random.randint(1,6)
3
>>> random.randint(1,6)
3
>>> random.randint(1,6)
6
>>> random.randint(1,6)
5
>>> random.randint(1,6)
1
>>> random.randint(1,6)
6
>>> random.randint(1,6)
4
>>> mins=input("Enter:")
Enter:hello
>>> mins
'hello'
>>> mins*10
'hellohellohellohellohellohellohellohellohellohello'
>>> mins=input("Enter:")
Enter:4
>>> mins*60
'444444444444444444444444444444444444444444444444444444444444'
>>> type(mins)
<class 'str'>
>>> m=int(mins)
>>> type(m)
<class 'int'>
>>> m
4
>>> mins
'4'
>>> m*60
240
>>> 'elapsed:'+(m*60)+'seconds'
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    'elapsed:'+(m*60)+'seconds'
TypeError: can only concatenate str (not "int") to str
>>> 'elapsed:'+str(m*60)+'seconds'
'elapsed:240seconds'
>>> m
4
>>> if m<10: print("small")

small
>>> m=100
>>> if m<10: print("small")

>>> if m<10:
	print("small")
	print("another")
	print("stop it")

	
>>> m=4
>>> if m<10:
	print("small")
	print("another")
	print("stop it")

	
small
another
stop it
>>> 