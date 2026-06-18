Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1,num2,num3=10,20,30
print(num1)
10
print(num2)
20
print(num1,num2,num3)
10 20 30
>>> num1,num2,nu3=10,10,10
>>> print(num1)
10
>>> print(nu3)
10
>>> num1=num2=num3=10
>>> print(num3)
10
>>> print(id(num3))
140734785266888
>>> print(id(num2))
140734785266888
>>> a,b=10,20
>>> print(id(a),(b))
140734785266888 20
>>> print(id(a),id(b))
140734785266888 140734785267208
>>> a,b=256,256
>>> print(id(a),id(b))
140734785274760 140734785274760
>>> a,b=257,257
>>> print(id(a),id(b))
1966296636464 1966296636464
>>> a,b=259,259
>>> print(id(a),id(b))
1966296636656 1966296636656
>>> a,b=10,20
>>> print(id(a),id(b))
140734785266888 140734785267208
>>> a,b=b,a
>>> print(id(a),id(b))
140734785267208 140734785266888
>>> print(a,b)
20 10
>>> print(a, b)
20 10
