# _*_ coding:utf-8 _*_
# coder: Wang Yuchao
# Time: 2021/5/2912:28
# File_Name: Queue.py
# Edit Tool: PyCharm

# 用Python列表实现队列结构
# 列表的0位置表示队列尾部，可以用insert插入元素
# 列表的最后作为队列的头部，可以用pop删除元素

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

q = Queue()
q.enqueue('cat')
