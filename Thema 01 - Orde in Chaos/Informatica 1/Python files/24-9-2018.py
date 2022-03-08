Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(list)
<class 'type'>
>>> type(type)
<class 'type'>
>>> x = 1245890
>>> for i in x:
	i

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for i in x:
TypeError: 'int' object is not iterable
>>> x = str(x)
>>> for i in x:
	i

	
'1'
'2'
'4'
'5'
'8'
'9'
'0'
>>> i
'0'
>>> for i in range(0, 4):
	i

	
0
1
2
3
>>> 
