#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# below for ctrl+c ctrl+v for new python file




# IO
#name = input('please entry a name:')
#print('Welcome:', name)

import sys

if __name__ == '__main__':
    print("__name__ == __main__")

print("sys.argv is : ", sys.argv)
print(sys.path)


print("1","2","3")

a = 170

if a < 169 :
    print("a < 169")
else:
    print("a is not less than 169")

print(True and a < 169)


n = ord("家")
print(n)
print("ord('真') is", ord("真"))
print('真'.encode('utf-8'))
#print('真'.encode('ascii'))

print('比特币当前价位是：%d' % 28100)

# multiline
print("""ji
jia\n\n
kkkk""")

print(r"""jjj
jjj\n\n""")




# list common usage

lst = list(range(10))
print(lst)
print(8 in lst)
lst[4] = 8
print(lst)
lst.sort()
print(lst)
lst.append(78)
lst.append(77)
print(lst)
lst.pop()
print(lst)
lst.insert(1,89)
print(lst)




#dict common usage
nd = {}
print(nd)
nd[6] = 'kkk'
nd['t'] = 'ttt'
print(nd)
print(nd['t'])
print(nd.get(6, -2))
print(nd.get(7, -2))
print(nd.get(7))
print(None == nd.get(7))

'''
for value in nd.values():
    print('for value in values:', value)
for d in nd:
    print('for d in nd:', d)
for k,v in nd.items():
    print("for k,v in nd.items:",k,v)

for k,v in enumerate(lst):
    print("for k,v in enumerate(lst):",k, v )
'''



#set common usage

s = set([1,2,3])
print(s)

s.add('t')
print(s)
s.remove(2)
print(s)

s1 = set(['t','y','u'])
print(s1)
print(s1 & s)
print(s1 | s)



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(34))




print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
# print([k + '=' + v for k, v in nd.items()])


import os
print([d for d in os.listdir('..')])

gene = (temp * temp for temp in range(20))
print(gene)
print(next(gene))




def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a + b
        n = n + 1
    return 'done'



genefib = fib(10)

for item in genefib:
    print('genefib items:', item)

import collections
print(isinstance(genefib,collections.Iterable))
print(isinstance(genefib,collections.Iterator))
print(isinstance([], collections.Iterator))




# map and reduce
def func1(value1):
    return value1 * value1

map1 = map(func1, list(range(12,20)))
print (map1)
#print(list(map1))


import functools
def func2(value1, value2):
    return value1 + value2

print(functools.reduce(func2, list(map1)))

print(func2.__name__)























