import datetime
# filter 过滤器
def is_palindrome(n):
    s = list(str(n))
    b= list( reversed(s))
    return s==b
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# reduce 和 map
from functools import reduce
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9}[s]
    return reduce(fn, map(char2num, s))
def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def fn1(x, y):
        return x/10  + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9}[s]
    n = s.index('.')
    s1 = s[:n]
    s2 = s[n+1:]
    return reduce(fn, map(char2num, s1)) + reduce(fn1, list( map(char2num, s2))[::-1])/10
print('str2float(\'123.456\') =', str2float('123.4567'))

def normalize(s):
    a = s.lower()
    b = a[0].upper() + a[1:]
    return b
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def axb(a,b):
        return a*b
    return reduce(axb,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return  t[1]
L2 = sorted(L,key=by_name,reverse=True)
print(L2)

# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax+=n
        return ax
    return sum
print(lazy_sum(1,2,3,4) == lazy_sum(1,2,3,4))
print(lazy_sum(1,2,3,4))

# 匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5])))

# 装饰器 decorator
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s() begin:' %func.__name__)
        func(*args,**kwargs)
        print("call end...")
    return wrapper

@log
def now():
    print(datetime.datetime.now())

now()

# 偏函数
import functools
int2 = functools.partial(int,base =2)
print(int2('100000'))