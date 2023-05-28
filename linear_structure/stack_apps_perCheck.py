# _*_ coding:utf-8 _*_
# coder: Wang Yuchao
# Time: 2021/5/2611:02
# File_Name: stack_apps_perCheck.py
# Edit Tool: PyCharm

# 匹配括号
# 算术表达式 (5+6)*(4-2)/(7+3)
# 编写一个算法，它从左到右读取一个算数表达式，然后判断其中的括号是否匹配
# 注意到相匹配的左括号与右括号出现的顺序相反，暗示着能够运用栈类来解决括号匹配问题
# 从一个空栈开始，从左到右依次读取表达式，遇到左括号就进栈，遇到右括号就将栈顶的左括号出栈以示完成一次匹配
# 在读取到右括号时，栈应该不能为空，需要出栈一个左括号与之匹配；且在处理完表达式后，栈应该是空的，表示全部匹配完毕

from stack import *

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

string = "4+(5*3)+()"
print(parChecker(string))
