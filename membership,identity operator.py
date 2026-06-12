Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #membership operator
>>> #checks whethea the value is available or not
>>> a=[1,2,3,4]
>>> b=5
>>> b in a
False
>>> 10 not in (1,20,70)
True
>>> 10 not in {1,20,70}
True
>>> 's' in 'satwika'
True
>>> a=satwika
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=satwika
NameError: name 'satwika' is not defined
>>> a='satwika'
>>> b='r'
>>> b in a
False
>>> 
>>> # Identity operator
>>> a=10
>>> b=20
>>> a is b
False
>>> a=10
>>> b=10
>>> a is b
True
>>> a=90
>>> d=a
>>> print(a is d)
True
lst1=[1,2]
lst2=[1,2]
lst1=lst2
print(lst1=lst2)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(lst1=lst2)
TypeError: print() got an unexpected keyword argument 'lst1'
print(lst1==lst2)
True
lst1 is lst2
True
