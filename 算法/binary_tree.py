class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 中序遍历
def left_mid_right(obj):
    if obj is None:
        return
    left_mid_right(obj.left)
    print(obj.value)
    left_mid_right(obj.right)


# 先序遍历
def mid_left_right(obj):
    if obj is None:
        return
    print(obj.value)
    mid_left_right(obj.left)
    mid_left_right(obj.right)

# 后序遍历
def left_right_mid(obj):
    if obj is None:
        return
    left_right_mid(obj.left)
    left_right_mid(obj.right)
    print(obj.value)

A = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
left_mid_right(A)
print('--')
mid_left_right(A)
print('--')
left_right_mid(A)