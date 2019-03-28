a = [9,1,3,5,11,56,32,6,78,24]

# 外层for循环
for i in range(len(a)-1):  # 有n个数，第一次将列表第0和第1个数比较大小，那么第n-1次是将第n-1个数和第n个数比较大小，所以需要循环n-1次
    is_change = True

    # 内层for循环
    for j in range(len(a)-i-1):  # 每经过一次外循环会将一个最大的数排列到列表最后方，所以内层循环只需要n-i-1次
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            is_change = False  # 如果在这次内循环中，存在后一个元素比前一个元素大的情况，那么需要继续排序，将is_change置为False
    if is_change:
        break
print(a)