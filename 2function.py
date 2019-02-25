a= abs
print(a(-10))
n1 = 255
n2 = 100
print("{}+ {}".format(hex(n1),hex(n2)))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

nums = [1,2,3]
print(calc(*nums))

# 关键字参数,可无限个输入参数
def calc1(**kw):
    return (kw)
temp = {"hello":"kaspar","bye":2018}
print(calc1(**temp))

# 命名关键字参数, 只接受 city和job作为关键字参数
def person(name, age, *, city, job):
    print(name ,age, city, job)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))