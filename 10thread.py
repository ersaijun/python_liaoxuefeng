# -*- coding : utf-8 -*-
# @Time      : 2019/2/21 10:59
# @Author    : Kaspar
# @File      :10thread.py

import time,threading,multiprocessing

# 新线程执行代码
def loop():
    print('thread {} is running...'.format(threading.current_thread().name))
    n = 0
    while n<5:
        n+=1
        print('thread {} >> {}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {} ended...'.format(threading.current_thread().name))

print('thread {} is running ...'.format(threading.current_thread().name))
t = threading.Thread(target=loop,name = 'LoopThread')
t.start()
t.join()
print('thread {} ended'.format(threading.current_thread().name))

###################################################################
# 来看看多个线程同时操作一个变量怎么把内容给改乱
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100):
        lock.acquire()
        change_it(n)
        lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

##########################################################
# 跑满CPU
print(multiprocessing.cpu_count())  # CPU 核数
def loop1():
    x = 0
    while True:
        x = x ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop1)
    t.start()

import re
print( re.split(r'[\s\,]+','a  ,  d    f  '))