# 链表：需要维护元素之间的相对位置，但是并不需要在“连续的内存空间”中维护这些位置信息
# 必须指明第一个元素的位置，这样可以根据链接信息访问后面的元素
# 指向链表第一个元素的引用称作头，最后一个元素需要知道自己没有下一个元素（Null）

# ADT抽象数据类型的实现 = 定义元素+操作 （数学里相当于定义集合及其上运算）
# 1. 节点类 （构建列表的基本数据元素）
# 2. 列表类 （节点的位置关系）
# 理解成节点是基本元素，且节点包含数据和指向下一节点的信息
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==None
    
    # 往已有的链表添加节点，因为链表遍历元素需要从头开始，选择将元素放在最简便的位置——头，把原链表链接在其后面
    def add(self, item):
        temp = Node(item) # 创建以item为数据项的节点
        temp.setNext(self.head)
        self.head = temp  # 头引用变成指向新添加节点

    # 接下来要实现的方法length search remove都基于链表遍历
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count
    
    def search(self, temp):
        current = self.head
        found = False
        while current!=None and found==False:
            if current.data==temp:
                found=True
            else:
                current = current.getNext()
        return found
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.search(17))
