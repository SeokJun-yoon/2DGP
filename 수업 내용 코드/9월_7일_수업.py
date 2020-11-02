Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> a=10.0
>>> type(a)
<class 'float'>
>>> a='hjfldsjfks'
>>> type(a)
<class 'str'>
>>> print(a)
hjfldsjfks
>>> a
'hjfldsjfks'
>>> a
'hjfldsjfks'
>>> a
'hjfldsjfks'
>>> 32+32
64
>>> a="hello 'world'"
>>> a
"hello 'world'"
>>> a='hello "world"'
>>> a
'hello "world"'
>>> a="hello \"world\""
>>> a
'hello "world"'
>>> 'jfl sdjfksld jfsldjfs'
'jfl sdjfksld jfsldjfs'
>>> a='Hello \'dave\' and "tom"'
>>> a
'Hello \'dave\' and "tom"'
>>> 
>>> 
>>> a=10
>>> a
10
>>> a=10,20
>>> a
(10, 20)
>>> a=10,10.0,'10'
>>> a
(10, 10.0, '10')
>>> x=10
>>> y=20
>>> x
10
>>> y
20
>>> pos=10,20
>>> pos
(10, 20)
>>> pos[0]
10
>>> pos[1]
20
>>> pos
(10, 20)
>>> (x1,y1)=pos
>>> x1
10
>>> y1
20
>>> createFont(style)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    createFont(style)
NameError: name 'createFont' is not defined
>>> style={'bold'}
>>> style=style|'italic'
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    style=style|'italic'
TypeError: unsupported operand type(s) for |: 'set' and 'str'
>>> style=style|{'italic'}
>>> style
{'bold', 'italic'}
>>> 
>>> 
>>> 
>>> style=style|{'bold'}
>>> style
{'bold', 'italic'}
>>> 