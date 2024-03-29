# 双端队列：一前一后两端，两端都可以添加和移除元素
# 假设双端队列的后端是列表的0位置

class Deque:  #是通过列表实现的，但我们在用它的时候，完全把它看成队列的逻辑结构
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]
    
    def addFront(self, item):
        self.items.append(item)  # 前端进行添加或删除的时间复杂度是O(1)

    def addRear(self, item):   
        self.items.insert(0,item) # 后端进行添加或删除的时间复杂度是O(n)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

# 回文问题：运用双端队列可以解决的一个经典问题
# 回文即正着读反着读是一样的，如radar, toot, wow
# 检查一个字符串是否回文，以体现双端队列的应用
# （其实用Python列表可以很容易实现，不过思路也完全类似双端队列，只不过问题比较简单，不明确定义双端队列来解决问题）

def palchecker(aString):
    charDeque = Deque()
    
    for char in aString:
        charDeque.addFront(char)

    flag = True
    while charDeque.size()>1:
        f = charDeque.removeFront()
        r = charDeque.removeRear()
        if f!=r:
            flag = False
            break
    return flag

strs = 'radar'
print(palchecker(strs))

