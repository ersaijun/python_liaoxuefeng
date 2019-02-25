# -*- coding : utf-8 -*-
# @Time      : 2019/1/30 9:52
# @Author    : Kaspar
# @File      :6class.py

# 在Python中，实例的变量名
# 如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name # 私有
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 98)
bart.name = "kaspar"
bart.age  = 20

# print(bart.__name)  # 错误
print(bart._Student__name)  # 可以，但不建议
bart.print_score()
print(bart.name )
print(dir("ABC"))