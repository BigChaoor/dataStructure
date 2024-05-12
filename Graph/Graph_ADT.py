# 邻接表是对稀疏图的一种高效存储方式
# 将所有图顶点保存到一个主列表，同时为每一个顶点对象都维护一个列表，其中记录与它相连的顶点

# 在Python中，通过字典可以轻松地实现邻接表。
# 创建两个类：Graph类存储包含所有顶点的主列表，Vertex类表示图中的每一个顶点
# 对Vertex类的实现中，我们采用字典（而非列表），键是顶点，值是权重

# 对于一个具体的图，我们先根据图结构创建Vertex类对象（字符记录顶点标签，字典记录相连的顶点），
# 然后通过创建Graph类对象将Vertex对象连在一个列表中

# Vertex类
class Vertex:
    def __init__(self, key):  # 构造函数，两个基本属性
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):  # 增加邻接顶点，权重给个默认初始值
        self.connectedTo[nbr] = weight

    def __str__(self):  # 打印出此顶点的所有邻接顶点信息
        return str(self.id)+'connectedTo:'+str([x.id for x in self.connectedTo]) # 键值是顶点
    
    def getConnections(self):
        return self.connectedTo.keys()   # dict.keys()以列表形式返回字典的所有键值
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# 凭借Vertex类实现Graph类
class Graph:
    def __init__(self):
        self.vertList = {}   # 顶点名映射到顶点Vertex类对象的字典
        self.numVertices = 0 # 顶点数量

    def addVertex(self,key): # 向图中添加顶点对象
        self.numVertices += 1
        newVertex = Vertex(key)  # 创建一个新的Vertex类对象
        self.vertList[key] = newVertex # 将新建的顶点对象加入到Graph中
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self): # 获取Graph的所有顶点
        return self.vertList.keys()  # dict.keys()以列表形式返回字典的所有键
      
    def __contains__(self,n):  # 判断Graph是否包含某个顶点
        return n in self.vertList
    
    def addEdge(self,f,t,cost=0): # 向图中添加边，通过调用Vertex类方法实现，f和t是这条边两个顶点的标签，cost是边的权重
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def __iter__(self):
        return iter(self.vertList.values()) # dict.values()以列表形式返回字典的所有值
    
