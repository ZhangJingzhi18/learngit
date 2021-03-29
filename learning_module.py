# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:59:54 2021

@author: HP
"""

'''
Python又引入了按目录来组织模块的方法，称为包（Package）
'''

' a test module'

__author__ = 'Michael Liao'

import sys
'''
args变量，用list存储命令行所有参数，
'''

'''
def test():
      args = sys.argv
      if len(args) == 1:
          print('Hello, world!')
      elif len(args) == 2:
          print('Hello, %s!' % args[1])
      else:
          print('Too many arguments!')

if __name__ == '__main__':
    test()
''' 
    
'''
python解释器把一个特殊变量__name__置为__main__,
如果在其他地方导入该hello模块，if判断将失败，
如果直接运行，将被执行，如果作为导入模块，不被执行
'''

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('zhang'))
print(greeting('ziv'))    



































































































































