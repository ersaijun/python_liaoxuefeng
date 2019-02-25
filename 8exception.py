# -*- coding : utf-8 -*-
# @Time      : 2019/2/18 10:43
# @Author    : Kaspar
# @File      :8exception.py

import logging
def foo(s):
    n = int(s)
    if n ==0:
        raise ValueError("value error")
    return 10 / n
def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        # logging.exception(e)
        print(e)

main()
print('END')

# 断言
# 凡是print()来辅助查看的地方，都可以用断言（assert）来替代
def foo2(s):
    n = int(s)
    assert n!=0,'n is zero'
    return 10/n
def main2():
    foo2('0')
# main2()

#################################
# 单元测试
import unittest
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('no this key {}'.format(str(item)))
    def __setattr__(self, key, value):
        self[key] = value

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empt

unittest.main()