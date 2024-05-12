# 广度优先搜索
# 应用场景：词梯问题

# 构建单词关系图，将只有一个字母之差且差别在同一个位置的单词存入一个字典（单词桶）
# 两两匹配的效率较低，设定一些共同的标签，然后将单词表中的单词逐一和标签对比
from Graph_ADT import *
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')  # 以读的方式打开wordFile
    # 创建词桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]  # 定义新的键值对，值是以word为元素的列表
    # 为同一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)

    return g



