# -*- coding : utf-8 -*-
# @Time      : 2019/2/21 8:53
# @Author    : Kaspar
# @File      :10process.py

###################################################
# 进程
import os,time,random
from multiprocessing import Process,Queue

print('process {} start'.format(os.getpid()))

# 子进程要执行的代码
def run(name):
    print('run child {} ({})'.format(name,os.getpid()))


if __name__ == '__main__':
    print('parent process {}'.format(os.getpid()))
    p = Process(target=run,args=('test',))
    print('child process will start..')
    p.start()
    p.join()  # 等待子进程结束再继续往下运行
    print('child process end')


# 子进程
# import subprocess
# print('look www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('exit code:',r)
#
# p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('exit code:',p.returncode)

# 进程间通信  提供 Queue、Pipes 等多种方式来交换数据
def write(q):
    print('process to write {}'.format(os.getpid()))
    for value in ['a','b','c']:
        print('put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('process to read {}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('get {} from queue'.format(value))

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动子进程pw 写入
    pw.start()
    # 启动子进程 pr 读取
    pr.start()

    pw.join()
    pr.terminate() # 因为是死循环，强制终