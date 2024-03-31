
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
