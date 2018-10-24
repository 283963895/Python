#coding=utf-8
'''拷贝与深层拷贝'''
import copy
a=[1,2,3,4,5,6,7]
b=a
print b
c=copy.deepcopy(a)
a[1] = 10
print a
print b
print c