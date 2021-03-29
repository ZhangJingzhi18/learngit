# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:28:39 2021

@author: HP
"""

'''
面向过程的程序设计
通过把大段代码拆成函数，通过一层一层的函数调用，
就可以把复杂任务分解成简单的任务，这种分解
'''
#Higher-order function
'''
def add(x, y, f):
    return f(x) + f(y)

a = add(-5, 6, abs)
print(a)
'''

#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回。
'''
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))#因为r是一个iterator，是惰性序列，因此list()函数将整个序列都计算出来
'''
'''
a = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)#这个list所有数字转为字符串
'''

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce
def fn(x, y):
    return x*10 + y
'''
#a = reduce(fn, [1,3,5,7,9])
#print(a)
''''
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9}    
    return digits[s]
a = reduce(fn, map(char2num, '13579'))
print(a)
'''
'''
#把字符串转化为整数的函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
a = str2int(DIGITS)
print(a)
'''
'''
def normalize(name):

    return name[0].upper()+name[1:].lower()

from functools import reduce

def prod(L):

    return reduce(lambda x,y:x*y,L)

Digits={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,".":"."}

def char2num(s):

    return Digits[s]

def str2float(s):

    L1=list(map(char2num,s))

    n=s.index(".")

    L1.pop(n)

    num=reduce(lambda x,y:10*x+y, L1)

    return num*10**(n-len(L1))
'''

'''
在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
a = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(a)
'''

'''
把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip() #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
a = list(filter(not_empty, ['a', '' ,'b', None, ' ' ]))
print(a)
'''

'''
#用埃氏筛法求素数

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x% n>0

def primes():
    yield 2 #先返回2
    it = _odd_iter()#初始序列
    while True:
        n = next(it)#返回初始序列第一个值
        yield n
        it = filter(_not_divisible(n), it)#构造新序列
        
#print the odd-num  in (1,100)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''

#lambda是匿名函数
#def sq(x):
#    return x * x
#a = map(sq, [y for y in range(10)])
#print(list(a))

#a = map(lambda x : x*x, [y for y in range(10)])
#print(list(a))
#lambda argument_list参数列表 :expersion参数的表达式

'''
import time
#测试的def函数
def square1(n):
    return n ** 2

#测试的lambda函数
square2 = lambda n: n ** 2

print(time.time())

#使用def函数
i = 0
while i<10000000:
    square1(100)
    i += 1
print(time.time())    
#使用lambda函数
i = 0
while i < 10000000:
    square2(100)
    i += 1
print(time.time())
'''
#c = lambda x, y, z: x*y*z
#a = c(2,3,4)
#print(a)
#squares = map(lambda x:x**3,range(5))
#print(list(squares))

#a = sorted([36,5,-15,9,-21])
#print(a)
#a = sorted([36,5,-12,9,-21], key = abs)
#print(a)
#a = sorted(['Bob', 'about', 'Zoo', 'credit'])
#print(a)
#
#b = sorted(['Bob', 'about', 'Zoo', 'credit'], key = str.lower)
#print(b)
#
#c = sorted(['Bob', 'about', 'Zoo', 'credit'],key=str.lower,reverse=True)
#print(c)
'''
L = [('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]
def by_name(t):
    return t[0].lower()#按小写的首字母排序

L2 = sorted(L, key=by_name)
print(L2)
'''
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return -t[1]#没有使用reverse，直接按倒数排序
L2 = sorted(L, key=by_score)
print(L2)
'''

#高阶函数可以把函数作为结果值返回
#def calc_sum(*args):
#    ax = 0
#    for n in args:
#        ax = ax + n
#    return ax
#def lazy_sum(*args):
#    def sum():
#        ax=0
#        for n in args:
#            ax=ax+n
#        return ax
#    return sum
#
#f = lazy_sum(1,3,5,7,9)
#print(f)
#print(f())
#当lazy_sum返回函数sum时，相关参数和变量
#都保存在返回的函数中，称为“闭包Closure”
#f1 = lazy_sum(1,3,5,7,9)
#f2 = lazy_sum(1,3,5,7,9)
#print(f1==f2)

'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3= count()
print(f1(),f2(), f3())
'''
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
'''

'''
def createCounter():
    def f():
        n = 1
        while True:
            yield n
            n = n + 1
        return n
    output = f()
    def counter():
        return next(output)
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''

#匿名函数有个限制，就是只能有一个表达式，
#不用写return，返回值就是该表达式的结果。
'''
f = lambda x: x*x
print(f(5))
'''
'''
def nonnamefunction(x):
    return x*x
print(nonnamefunction(5))
'''
#def build(x, y):
#    return lambda: x*x + y*y
#L = list(filter(lambda n: n%2 ==1, range(1,20)))
#print(L)
#def now():
#    print('2015-3-25')
#f = now
#f()
#print(now.__name__)
#print(f.__name__)


#装饰器Decorator
#在代码运行期间动态增加功能
#def log(func):
#    def wrapper(*args, **kw):
#        print('call %s():' % func.__name__)
#        return func(*args, **kw)
#    return wrapper
#@log
#def now():
#    print('2015-3-25')

#now()
#now = log(now)

#def log(text):
#    def decorator(func):
#        def wrapper(*args, **kw):

'''
def hi(name = 'yasoob'):
    return 'hi ' + name
#print(hi())
greet = hi
#print(greet())
del hi
#print(hi())

print(greet())
'''
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
'''


'''
#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time.functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        s_time = time.time()#记录时间
        f = fn(*args, **kw)
        e_time = time.time()#结束时间
        print('%s  excuted in %s ms' % (fn.__name__, e_time-s_time))
        return f
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
'''


#functools模块提供了偏函数（Partial function）
#int()函数提供base参数，默认为
#a = int('123456',base=8)
#print(a)
#a = int('123456',16)
#print(a)
#def int2(x, base=2):
#    return int(x, base)
#print(int2('100000'))
'''import functools'''
#int2 = functools.partial(int, base=2)
#functools.partial建立一个偏函数，不许定义int2()
'''
functools.partial将一个函数的某些参数固定住，返回一个新的函数

print(int2('100000'))
print(int2('100101010'))
'''
'''
max2 = functools.partial(max,10)
print(max2(5,6,7))'''
#把10作为*args的一部分自动加到左边
#args = (10,5,6,7)
#max(*args)

'''
当函数的参数个数过多时，用functools.partial创建一个新函数，固定部分参数，调用更为简单
'''





























































































































