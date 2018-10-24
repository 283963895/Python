#!/usr/bin/python
# coding=utf-8
'''私有化和property'''


class Test():
    def __init__(self):  #self表示类的实例 类似this
        self.__num = 100  #这里表示私有化属性值，是不能再外部使用的

    def setNum(self, num):  # 将self.__num的属性封装。
        self.__num = num

    def getNum(self):  # 获取__num的值。
        return self.__num
t = Test()
print(t.getNum())  # 将会出错，表示输出私有属性，外部无法使用。
t.__num = 200  # 这里将会理解为添加属性 __num = 200,而不是重新赋值私有属性。
print(t.__num)  # 这里输出的200是定义的属性__num，而不是self.__num。
t.setNum(200)  # 通过set方法将私有属性重新赋值。
t.getNum()  # 通过get方法获取__num的值。
print(t.getNum())
t.num = 300  # 调用类属性num,并重新赋值，porperty会自动检测set方法和get方法，并将引用赋值给set方法。
print(t.num)  # 输出类属性，并会自己检测使用get方法进行输出。
print t
t.sums = 10000
