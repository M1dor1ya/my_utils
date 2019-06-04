#  分而治之，递归
def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data)//2]
        left = []
        right = []
        data.remove(mid)
        for i in data:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data