
# 用递归实现将整数转换成以2~16为进制基数的字符串

def toStr(n, base):
    converString = '0123456789ABCDEF'
    if n<base:
        return converString[n]
    else:
        return toStr(n//base, base) + converString[n%base]  # 注意拼接顺序，类似栈的数据结构
    
print(toStr(123,2))

# 利用栈的数据结构递归实现
import stack
rStack = stack.Stack()
def toStrStack(n,base):
    converString = '0123456789ABCDEF'
    if n<base:
        rStack.push(converString[n])
    else:
        rStack.push(converString[n%base])
        toStrStack(n//base, base)

toStrStack(123,2)
s = ''
while not rStack.isEmpty():
    s = s+rStack.pop()

print(s)

# 用turtle模块递归地绘制螺旋线
from turtle import *
myTurtle = Turtle()  # 创建画图小乌龟
myWin = myTurtle.getscreen()

def drawSpiral(myTurrle, lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 100)
# myWin.exitonclick()
    
# 递归绘制分形树
def tree(branchLen, t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

t = Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()

# 汉诺塔问题
def moveTower(height:int, fromPole:str, toPole:str, withPole:str):
    '''
    height是正整数, 其他3个参数是字符串类型
    '''
    if height>=1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp,tp):
    print('moving disk from', fp, 'to', tp)
    
print('-----------汉诺塔方案: 5个盘子------------')
moveTower(5, 'the fist pole', 'the third pole', 'the second pole')


# 动态规划算法解决找零问题
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents  # 初始化为全用1分的硬币
        newCoin = 1   # 新使用的硬币初始化为1
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
        return minCoins[change]
    
def printCoins(coinsUsed, change):
    coin = change
    while coin>0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin-thisCoin

cl = [1,5,10,21,25]
coinsUsed = [0]*64
coinCount = [0]*64
dpMakeChange(cl, 63, coinCount, coinsUsed)
print(coinsUsed)        
printCoins(coinsUsed, 63)
