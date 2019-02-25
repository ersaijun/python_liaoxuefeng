from  collections import Iterable
print( isinstance('abc',Iterable))

for i,value in enumerate([1,2,3]):
    print(i ,value)

L1 = ['Hello', 'World', 18, 'Apple', None]
result = [s.lower() for s in L1 if isinstance(s,str)]
print(result)

# 生成器
g = (x*x for x in range(10))  # 是括号
for n in g:
    print (n)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'
for n in fib(10):
    print (n)

#  杨辉三角
def triangles():
    result = [1]
    while True:
        yield result
        result.append(0)
        result = [result[i-1]+result[i] for i in range(len(result))]
n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break