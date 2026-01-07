Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[1,2,3,4]
>>> a.count(1)
1
>>> a.count(2)
1
>>> a.append(5)
>>> print(a)
[1, 2, 3, 4, 5]
>>> a.index(5)
4
>>> a.index(2)
1
>>> a.pop(2)
3
>>> print(a)
[1, 2, 4, 5]
>>> a.reverse()
>>> print(a)
[5, 4, 2, 1]
>>> a.remove(4)
>>> print(a)
[5, 2, 1]
>>> a.remove(5)
>>> a.remove(2)
>>> print(a)
[1]
>>> a.insert(1,2)
>>> print(a)
[1, 2]
>>> b=['mango','pineapple','apple']
>>> a.extend(b)
>>> print(a)
[1, 2, 'mango', 'pineapple', 'apple']
>>> x=a.copy()
>>> print(x)
[1, 2, 'mango', 'pineapple', 'apple']
>>> a.clear()
>>> print(a)
[]
>>> c=('T','P','c')
c.count('T')
1
c.count('p')
0
c.count('P')
1
myset={'tomato','potato','carrot'}
mysetb={'onion','cucumber'}
mysetb.add('tomato')
c=myset.differnce(mysetb)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c=myset.differnce(mysetb)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
c=myset.difference(mysetb)
print(c)
{'carrot', 'potato'}
myset.difference_update(mysetb)
print(myset)
{'carrot', 'potato'}
mysetb.difference_update(myset)
print(mysetb)
{'cucumber', 'tomato', 'onion'}
print(myset)
{'carrot', 'potato'}
myset.add('orange')
myset.add('grapes')
mysetb.add('banana')
print(mysetb)
{'banana', 'cucumber', 'tomato', 'onion'}
mysetb.difference_update(myset)
print(mysetb)
{'banana', 'cucumber', 'tomato', 'onion'}

KeyboardInterrupt
 x=[1,2,3,4,5]
 
SyntaxError: unexpected indent
X=[1,2,3,4,5]
print(x[2])
mango
print(X[2])
3
X.insert(2,7)
print(X)
[1, 2, 7, 3, 4, 5]
 X*5
 
SyntaxError: unexpected indent
X*5
[1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5]
for a in X:
    print(a)

    
1
2
7
3
4
5
X.remove(4)
print(X)
[1, 2, 7, 3, 5]
