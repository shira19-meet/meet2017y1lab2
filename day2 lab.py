Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b=a
>>> b
10
>>> 
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> a=5
>>> b=10
>>> c=a
>>> c
5
>>> a=b
>>> a
10
>>> b
10
>>> c
5
>>> b=c
>>> a
10
>>> b
5
>>> c
5
>>> four='4'
>>> print(four*3)
444
>>> 
>>> five=4
>>> print(five*3)
12
>>> my_name='student'
>>> print("Hi,"+myName')
      
SyntaxError: EOL while scanning string literal
>>> i = "hello"
>>> l = "everybody"
>>> i + l
'helloeverybody'
>>> 'helloeverybody'
'helloeverybody'
>>> 
>>> my_age=15
>>> print('I am'+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print('I am'+my_age+'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> my_age='15'
>>> print('i am '+my_age+'years old')
i am 15years old
>>> score=1
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> 
==== RESTART: /home/student/shira19_lab2/meet2017y1lab2/squareinTurtle.py ====
>>> 
