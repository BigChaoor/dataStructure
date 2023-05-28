# _*_ coding:utf-8 _*_
# coder: Wang Yuchao
# Time: 2023/5/2810:48
# File_Name: stack.py
# Edit Tool: PyCharm

# 明确栈抽象数据类型的定义，用Python实现栈数据结构
# 和其他面向对象编程语言一样，需要在Python中实现像栈这样的ADT，就可以创建新类，栈的操作用方法实现
# 栈完全可以利用Python提供的强大简单的原生集合来实现，比如列表
# 利用列表实现栈类，一个比较合理的假定是列表的尾部作为顶端

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# 栈类的实例
s = Stack()
s.push(4)
s.push('cat')
