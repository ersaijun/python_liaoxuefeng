# -*- coding : utf-8 -*-
# @Time      : 2019/2/19 9:57
# @Author    : Kaspar
# @File      :9file.py
import  os
import  os.path

#  麻烦
f = open(os.path.abspath('.') +'/text.txt', 'r')
print(f.read())
f.close()

# with 方式
with open('F:/Project/python_test/text.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

####################################################

print(os.path.abspath('.'))
a = [x for x in os.listdir('.') if os.path.isdir(x)]  # 所有目录
print(a)
b = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  # 所有 py 文件
print(b)

####################################################
# JSON
import json
class Student(object):
    def __init__(self,name,age,score):
        self._name = name
        self._age = age
        self._score = score

s = Student('kaspar',20,88)
print(json.dumps(s,default=lambda obj:obj.__dict__))
//修改文件测试 git