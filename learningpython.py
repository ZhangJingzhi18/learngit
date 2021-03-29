# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:23:27 2021

@author: HP
"""
#L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#s = [L[0], L[1], L[2]]
#print(s)
#r = []
#n = 3
#for i in range(n):
#    r.append(L[i])
#    
#print(r)
#s = L[-2:]
#print(s)
#s = 'ASDFGHJKL'[::2]
#print(s)
#d = {'a':1, 'b':2, 'c':3}
#for k,v in d.items():
#    print(k)
#    print(v)
#for ch in 'ABCD':
#    print(ch)
#for i, v in enumerate(['A', 'B', 'C']):
#    print(i,v)
#for x, y in [(1,1), (2,4), (3,9)]:
#    print(x, y)
#def findMinAndMax(L):
#    if L!=[]:
#        (max,min)=(L[0],L[0])
#        for x in L:
#            if x> max:
#                max=x
#            if x< min:
#                min=x
#        return(max,min)
#    else:
#        return(None, None)
#a= list(range(1,11))
#L = []
#for x in range(1,11):
#    L.append(x * x)
#循环太麻烦，列表生成式
#a = [x * x for x in range(1, 11) if x % 2 == 0]
#print(a)
#a = [m + n for  m in 'ABC' for n in 'XYZ']
#print(a)

#import os
#a = [d for d in os.listdir('.')]
#print(a)
#d = {'x':'A', 'y':'B', 'z':'C'}
#for k, v in d.items():
#    print(k, '=', v)
#e = [k + '=' + v for k, v in d.items()]
#print(e)
#L = ['Hello', 'World', 'IBM', 'Apple']
#a = [s.lower() for s in L]
#print(a)
#a = [x if x % 2 == 0 else -x for x in range(1,11)]
#print(a)
'''
在列表生成式中
for 前面的 if~~~else是表达式。而for后面的if是过滤条件，不能带else
'''
#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = []
#[L2.append(s.lower()) for s in L1 if isinstance(s,str)]

'''列表元素按规则生成，循环过程中不断生成后续元素，不必创建完整list，节省大量空间，边循环边计算的机制，称为生成器：generator
'''
#L = [x * x for x in range(10)]
#g = (x * x for x in range(10))
#for n in g:
#    print(n)
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)
'''
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b #函数定义中包含yield关键字，函数就是一个generator
        a, b = b, a + b
        n = n +1
    return 'done'
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''

'''
def odd():
    print('step 1')
    print(1)
    yield 
    print('step 2')
    print(3)
    yield
    print('step 3')
    print(5)
    yield
    
o = odd()
next(o)
next(o) 
next(o)
'''
'''
#杨辉三角
L = [[1],[1,1]]
print(L[1])
c = input('input the num of layer:')
print(c)
cen = int(c)

def triangles(L, cen):
    n = 3
    while n <= cen:
        for i in range(0, n-1):
            L.append([])
            if i ==0:
                L[n-1].append(1)
                L[n-1].append(1)
            else:
                L[n-1].insert(i,L[n-2][i]+L[n-2][i-1])
        n = n+1
    return 'done'

triangles(L, cen)

for i in range(cen):
    print(L[i])
'''


'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：
'''

#from collections.abc import Iterable
#a = isinstance(100, Iterable)
#print(a)

'''python的Iterator对象表示一个数据流，Iterator对象可以被
next()调用不断返还下一个数据，知道没有数据返回StopIteration错误
Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而list永远不能存储全体自然数
'''
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break





















