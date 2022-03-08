Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_str = "hallo"
>>> type(my_str)
<class 'str'>
>>> for i in my_str:
	print(i)

	
h
a
l
l
o
>>> dna = "gatc"
>>> seq = "tttaaccg"
>>> for i in seq:
	i in dna

	
True
True
True
True
True
True
True
True
>>> seq = "tttaaqcg"
>>> for i in seq:
	i in dna

	
True
True
True
True
True
False
True
True
>>> for i in seq:
	i

	
't'
't'
't'
'a'
'a'
'q'
'c'
'g'
>>> my_int = 2000455
>>> for i in my_int:
	i

	
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for i in my_int:
TypeError: 'int' object is not iterable
>>> my_str = str(my_int)
>>> my_str
'2000455'
>>> my_list = ["hallo", "mijn", "naam", "is", "Niek"]
>>> type(my_list)
<class 'list'>
>>> my_list[0]
'hallo'
>>> my_list[4]
'Niek'
>>> my_list[-1]
'Niek'
>>> item = my_list[-1]
>>> item
'Niek'
>>> type(item)
<class 'str'>
>>> my_slice = my_list[1:3]
>>> my_slice
['mijn', 'naam']
>>> my_slice = my_list[1:4:2]
>>> my_slice
['mijn', 'is']
>>> my_list[:3]
['hallo', 'mijn', 'naam']
>>> my_list[3:]
['is', 'Niek']
>>> my_slice = my_list[-1:0:-1]
>>> my_slice
['Niek', 'is', 'naam', 'mijn']
>>> my_slice = my_list[-1::-1]
>>> my_slice
['Niek', 'is', 'naam', 'mijn', 'hallo']
>>> dir(my_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(my_list.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> my_list.reverse()
>>> my_list
['Niek', 'is', 'naam', 'mijn', 'hallo']
>>> my_list = ["hallo", "mijn", "naam", "is", "Niek"]
>>> my_list
['hallo', 'mijn', 'naam', 'is', 'Niek']
>>> reversed_list = my_list[::-1]
>>> reversed_list
['Niek', 'is', 'naam', 'mijn', 'hallo']
>>> my_list
['hallo', 'mijn', 'naam', 'is', 'Niek']
>>> my_list[4]
'Niek'
>>> my_list[::4]
['hallo', 'Niek']
>>> my_list[4:]
['Niek']
>>> students = ["Sander", "Melvin" ,"Niek"]
>>> students.apend("Joshua")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    students.apend("Joshua")
AttributeError: 'list' object has no attribute 'apend'
>>> students.append("Joshua")
>>> students
['Sander', 'Melvin', 'Niek', 'Joshua']
>>> studensts = students + ["Hugo", "Gijs"]
>>> students
['Sander', 'Melvin', 'Niek', 'Joshua']
>>> students = students + ["Hugo", "Gijs"]
>>> students
['Sander', 'Melvin', 'Niek', 'Joshua', 'Hugo', 'Gijs']
>>> sorted(students)
['Gijs', 'Hugo', 'Joshua', 'Melvin', 'Niek', 'Sander']
>>> my_sorted_list = sorted(students)
>>> my_sorted_list
['Gijs', 'Hugo', 'Joshua', 'Melvin', 'Niek', 'Sander']
>>> my_str = "abBA"
>>> sorted(my_str)
['A', 'B', 'a', 'b']
>>> ord("a)
	
SyntaxError: EOL while scanning string literal
>>> ord("a")
	
97
>>> ord("A")
	
65
>>> students
	
['Sander', 'Melvin', 'Niek', 'Joshua', 'Hugo', 'Gijs']
>>> students.remove('Hugo')
	
>>> students
	
['Sander', 'Melvin', 'Niek', 'Joshua', 'Gijs']
>>> students.pop(0)
	
'Sander'
>>> students
	
['Melvin', 'Niek', 'Joshua', 'Gijs']
>>> dna
	
'gatc'
>>> dna[0] = "u"
	
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dna[0] = "u"
TypeError: 'str' object does not support item assignment
>>> dna_list = ["g", "a", "t", "c"]
	
>>> dna_list[0] + "u"
	
'gu'
>>> dna_list
	
['g', 'a', 't', 'c']
>>> 
	
>>> dna_list[0] = "u"
	
>>> dna_list
	
['u', 'a', 't', 'c']
>>> dna = "gatc"
	
>>> dna = "uatc"
	
>>> dna
	
'uatc'
>>> 

>>> monkaS
	
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    monkaS
NameError: name 'monkaS' is not defined
>>> #oefenen op CodeAcademy en Sololearn
	
>>> dir(students)
	
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(students.sort)
	
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> my_tuple("aap", "noot", "mies")
	
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    my_tuple("aap", "noot", "mies")
NameError: name 'my_tuple' is not defined
>>> my_tuple = ("aap", "noot", "mies")
	
>>> type(my_tuple)
	
<class 'tuple'>
>>> my_dict = {"Jurre": "06987654", "Niek": "0615318888", "Sander": "0621676288"}
	
>>> my_dict
	
{'Jurre': '06987654', 'Niek': '0615318888', 'Sander': '0621676288'}
>>> my_dict['Jurre']
	
'06987654'
>>> my_dict['Niek']
	
'0615318888'
>>> my_dict['Sander']
	
'0621676288'
>>> my_dict['Melvin'] = "098373728"
	
>>> my_dict
	
{'Jurre': '06987654', 'Niek': '0615318888', 'Sander': '0621676288', 'Melvin': '098373728'}
>>> del my_dict['Melvin']
	
>>> my_dict.update({"Jurre":"042876328732974", "Rienk":"0912037143"})
	
>>> my_dict
	
{'Jurre': '042876328732974', 'Niek': '0615318888', 'Sander': '0621676288', 'Rienk': '0912037143'}
>>> comp_basen = {"a":"t", "t":"a"}
	
>>> mol_mass = {"a":55, "t":33}
	
>>> 
