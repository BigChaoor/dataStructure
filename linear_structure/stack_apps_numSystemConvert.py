# _*_ coding:utf-8 _*_
# coder: Wang Yuchao
# Time: 2023/5/2811:49
# File_Name: stack_apps_numSystemConvert.py
# Edit Tool: PyCharm

# 整数在计算机中以二进制存储
# 计算机如何实现十进制到二进制表达方式的转换？
# 除以2的算法，将原数不断除以2，这个过程所得的余数的逆序就是二进制表达
# 反转特性利用栈来解决问题

from stack import *

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(233))
