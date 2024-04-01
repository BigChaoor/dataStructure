# 排序
# 冒泡排序: 被认为是效率最低的排序算法
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        flag = True
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                flag = False
        if flag:
            break
    # return alist

noOrderlist1 = [9, 1, 20, 13, 4, 8]
bubbleSort(noOrderlist1)
print(noOrderlist1)

# 选择排序：在冒泡排序的基础上做了改进，减少了交换次数
def selectionSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        indexofMax = 0
        for location in range(1,passnum+1):
            if alist[location]>alist[indexofMax]:
                indexofMax = location
        alist[passnum],alist[indexofMax] = alist[indexofMax],alist[passnum]

noOrderlist2 = [9, 1, 20, 13, 4, 8]
selectionSort(noOrderlist2)
print(noOrderlist1)

# 插入排序，复杂度也是O(n**2)

# 希尔排序：对插入排序做了改进，将列表分成数个子列表，并对每一个子列表用插入排序
# 如何切分列表是希尔排序的关键，并不是连续切分，而是使用增量选取
# 使用分治策略，递归算法，每次将一个列表一分为二，并对两个部分都递归调用归并排序，当两部分都有序后，就进行归并
# 复杂度O(nlog(n))


# 快速排序：也采用分治策略，先选出一个基准值，然后用双指针以基准值为界划分列表，对左右两部分子表递归调用快排
# 基准值的选取影响算法复杂度，一般采用三数取中法



