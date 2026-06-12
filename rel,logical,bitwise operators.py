Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #relational operator
>>> a=5
>>> b=10
>>> print(a>b)
False
>>> 5>10
False
>>> 10<8
False
>>> 8<10
True
>>> 5<=10
True
>>> 10>=20
False
>>> 10==9.9
False
>>> 10!=19
True
>>> 'A'>'a'
False
>>> 
>>> 
>>> #logical operator
>>> (10>5)or(10<11)
True
>>> 10==10and10>=9
SyntaxError: invalid decimal literal
>>> 10== 10and10>= 9
SyntaxError: invalid decimal literal
>>> (10== 10)and(10>= 9)
True
>>> not(1.96<1.97)and(20==20.00)
False
>>> (10)and(5)
5
a=10
b=5
(a)or(b)
10


#bitwise operators
a=20
b=15
print(a+b)
35
print(a/b)
1.3333333333333333
print(a^b)
27
10/2
5.0
10>>2
2
32>>1
16
32>>2
8
32>>3
4
32>>5
1
10<<2
40
