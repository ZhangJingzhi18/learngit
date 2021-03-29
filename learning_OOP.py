# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:28:14 2021

@author: HP
"""

'学习 面向对象编程--Object Oriented Programming'
'''
面向过程的程序设计把计算机程序视为一系列的命令集合
把函数切分为子函数，降低系统的复杂度
面向对象的程序设计把计算机程序视为一组对象的集合
每个对象接受其他对象发来的消息，消息在各个对象之间传递
'''
#自定义的对象数据类型就是面向对象的类（class）的概念

'''
class St(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' %(self.name, self.score))
        
bart = St('Bart Simpson', 59)
Lisa = St('Lisa Simpson', 87)
bart.print_score()
Lisa.print_score()
'''


'''
面向对象的设计思想是抽象出class ,根据class创建instance
'''
'''
class St(object):
    pass
bart = St()
'''
#print(bart)
#print(St)
#bart.name = 'Bart simpson'
#print(bart.name)
'''
在创建实例的时候，把必须绑定的属性强制填写，定义特殊的__init__
'''

'''
class St(object):
    def __init__(self, name, score):
        self.name =name
        self.score =score
#self表示创建的实例本身，在__init__方法内部，把各种属性绑定在
#self，self指向创建的实例本身

bart = St('bart simpson', 59)
print(bart.name)
print(bart.score)

#面向对象的重要特点就是数据封装
def print_score(std):
    print('%s:%s' % (std.name, std.score))
print_score(bart)

'''

'''
直接在St类的内部定义访问数据的函数
'''

'''
class St(object):
    def __init__(self, name, score):
        self.name = name
        self.score =score
        
    def print_score(self):
        print('%s:%s' % (self.name, self.score))
bart = St('bart simpson', 59)      
bart.print_score()
'''

'''
class St(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = St('Lisa', 99)
bart = St('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
'''

'''
class St(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = St('Bart', 59)
'''


#print(bart._St__name)
'''
不能直接访问__name是因为python将其改成了
_St__name，可以用_St__name来访问变量
'''
#print(bart.get_name())
'''
bart.__name = 'New Name'
print(bart.__name)
'''
#外部代码成功设置了__name变量，但这个__name变量和class内部
#__name变量不是一个变量
#外部代码给bart新增了一个__name变量
#print(bart.get_name())

'''
class St(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        
    def get_gender(self):
        return self.__geender
    
    def set_gender(self, gender):
        self.__gender = gender
        
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
'''

'''
        继承和多态
'''
#新的class称为子类(Subclass)
#而被继承的class称为基类、父类或超类(Base class、Super class)


'''
class Animal(object):
    def run(self):
        print("Animal is running```")
#需要编写Dog和Cat类时，就可以直接从Animal类继承
#子类获得了父类的全部功能
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()
cat = Cat()
cat.run()
#由于Animial实现了run()方法
#Dog和Cat作为它的子类
#自动拥有了run()方法
'''
'''
class Dog(Animal):
    def run(self):
        print('Dog is running```')
        
    def eat(self):
        print('Eating meat```')

class Cat(Animal):
    def run(self):
        print('cat is running```')
        
dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()
'''

#当子类和父类都存在run()时
#子类的run()覆盖了父类的run()
#代码调用的都是子类的run()
#子类继承的另一个好处：多态

'''
a = list()
b = Animal()#b是Animal类型
c = Dog()#c是Dog类型
aa =isinstance(a, list)
print(aa)
bb =isinstance(b, Animal)
print(bb)
cc =isinstance(c, Dog)
print(cc)
cc2 =isinstance(c, Animal)
print(cc2)#c还可以是Animal
bb2 =isinstance(b, Dog)
print(bb2)
'''

'''
        多态
'''
#import abc
#class Animal(metaclass=abc.ABCMeta):#同一种事物：动物
#    @abc.abstractmethod
#    def talk(self):
#        pass
#
#class Cat(Animal):#动物的形态之一
#    def talk(self):
#        print('say miaomiao')
#        
#class Dog(Animal):#动物的形态之一
#        def talk(self):
#            print('say wangwang')
#            
#class Pig(Animal):
#    def talk(self):
#        print('say aoao')
#
##多态性是指具有不同功能的函数可以使用相同的函数名，
##可以用一个函数名调用不同内容的函数
#c = Cat()
#d = Dog()
#p = Pig()
#
#def func(obj):
#    obj.talk()
#
#func(c)
#func(d)
#func(p)

'''
多态性：一个接口，多种实现
'''
        
'''
鸭子类型是动态类型的一种风格
一个对象有效的语义，不是由继承自
特定的类或实现特定的接口，而是由“当前方法
和属性的集合”决定
When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck
'''
#class Duck():
#    def walk(self):
#        print('I walk like a duck')
#    def swim(self):
#        print('i swim like a duck')
#
#class Person():
#    def walk(self):
#        print('this one walk like a duck') 
#    def swim(self):
#        print('this man swim like a duck')


'''
获取对象信息
'''

#print(type(123))
#print(type('str'))
#print(type(None))
#print(type(abs))
#print(type(a))

#a = type(123) ==type(456)
#print(a)
#a = type(123) == int
#print(a)
#a = type('123') == type('abc')
#print(a)
#a = type('abc') == str
#print(a)
#a = type('abc') == type(123)
#print(a)

#import types
#def fn():
#    pass

#a = type(fn) == types.FunctionType
#print(a)
#a = type(abs) == types.BuiltinFunctionType
#print(a)
#a = type(lambda x:x) == types.LambdaType
#print(a)
#a = type((x for x in range(10))) == types.GeneratorType
#print(a)
    
#a = dir('ABC')
#print(a)
#b = len('ABC')
#print('b:',b)
#c = 'ABC'.__len__()
#print('c:',c)

#class Mydog(object):
#    def __len__(self):
#        return 100
#dog = Mydog()
#print(len(dog))

#class MyObject(object):
#    def __init__(self):
#        self.x = 9
#    def power(self):
#        return self.x * self.x

#obj = MyObject()
#a = hasattr(obj, 'x')#有属性"x"?
#print(a)
#print(obj.x)
#b = hasattr(obj, 'y')
#print(b)
#setattr(obj,'y', 19)#设置一个属性y
#c = hasattr(obj, 'y')
#print(c)
#cc = getattr(obj, 'y')#获取属性“y”
#print(cc)
#print(obj.y)

#a = getattr(obj, 'z', 404)#获取属性“z”，如果不存在，返回默认值404
#print(a)

#fn = getattr(obj, 'power')
#print(fn)
#print(fn())

#def readImage(fp):
#    if hasattr(fp, 'read'):
#        return readData(fp)
#    return None

'''
        实例属性和类属性
根据类创建的实例可以任意绑定属性

'''
#给实例绑定属性的方法是通过实例变量，或者通过self变量
#class St(object):
#    def __init__（self, name）:
#        self.name = name
#
#s = St('Bob')
#s.score = 90

#如果Student类本身需要绑定一个属性呢？
#可以直接在class中定义属性，这种属性是类属性，归Student类所有
class St(object):
    name = 'St'

s = St()#创建实例s
print(s.name)#打印name属性,因为实例并没有name属性,所以继续查找class的name属性
print(St.name)
s.name = 'Michael'#给实例绑定name属性
print(s.name)
#由于实例属性优先级比类属性高，因此
#实例属性会屏蔽name属性
print(St.name)#类属性并没有改变
del s.name
print(s.name)#再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了



















































