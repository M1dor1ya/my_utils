class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# �������
def lmg(obj):
    if obj is None:
        return
    lmg(obj.left)
    print(obj.value)
    lmg(obj.right)


# �������
def mlg(obj):
    if obj is None:
        return
    print(obj.value)
    mlg(obj.left)
    mlg(obj.right)

# �������
def lrg(obj):
    if obj is None:
        return
    lrg(obj.left)
    lrg(obj.right)
    print(obj.value)

A = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
lmg(A)
print('--')
mlg(A)
print('--')
lrg(A)