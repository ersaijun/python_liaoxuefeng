# -*- coding: utf-8 -*-
# 1.2
print(ord("赛"))

print('ABC'.encode('ascii'))
print('张赛'.encode('utf-8'))
print(b'\xe5\xbc\xa0\xe8\xb5\x9b'.decode('utf-8'))

print('hello,{},good bye {}'.format("kaspar",'2018'))
print("hello %s, nice to meet you  %d " % ('kaspar',2019))

s1 = 72
s2 = 85
print( "grade %.2f" % (int(s2)-int(s1)/int(s2)))

# 1.3
print((2,))
# num =1
# while True:
#     print(num)
#     num+=1
print(set([1,2]))