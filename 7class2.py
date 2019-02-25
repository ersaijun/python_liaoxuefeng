# -*- coding : utf-8 -*-
# @Time      : 2019/1/30 15:29
# @Author    : Kaspar
# @File      :7class2.py
class Student(object):
    __slots__ = ('name', 'age','score') # 用tuple定义允许绑定的属性名称

s= Student()
s.name = 'kaspar'
s.age = 20
s.score = 20
# s.school = "BUAA" # 错误，未绑定该属性

class GraduateStudent(Student):
    pass    # 在继承中，父类绑定的属性对子类不起作用
g = GraduateStudent()
g.school = "BUAA"

print(g.school)

################################################
#  @property 装饰器把一个方法变成属性调用
class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s2 = Student2()
s2.score = 60  #  实际转换为 s2.set_score(60)
print(s2.score)   #  实际转换为 s2.get_score()
# s2.score =999

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an interger!')
        if value < 0 :
            raise ValueError('width must above 0')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an interger!')
        if value < 0 :
            raise ValueError('score must above 0')
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

sc = Screen()
sc.width = 1024
sc.height = 768
print(sc.resolution)
assert sc.resolution == 786432, '1024 * 768 = %d ?' % sc.resolution

################################################
#  __str__() __repr__()  返回字符串作为类的名字
#  __iter__()  迭代对象
#  __getitem__() 下标取数据
#  __getattr__() 获取属性
class Fib(object):
    def __init__(self):
        self.a, self.b = 0 , 1

    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a,b = 1,1,
        for x in range(item):
            a,b = b,a+b
        return a

    def __str__(self):
        return "Fib object"
    __repr__ = __str__

for n in Fib():
    print(n)
print(Fib())
print(Fib()[6])

################################################
# 枚举类
from enum import Enum,unique
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique # 检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1 == Weekday(1))

