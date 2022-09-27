from string import ascii_uppercase

alpha = list(ascii_uppercase)


def preorder(start):
    if start != '.':
        print(start, end='')
        if tree[start][0] != '.':
            preorder(tree[start][0])
        if tree[start][1] != '.':
            preorder(tree[start][1])
    print()


def postorder(start):
    if start != '.':
        if tree[start][0]:
            postorder(tree[start][0])
        if tree[start][1]:
            postorder(tree[start][1])
        print(start, end='')
    print()


def inorder(start):
    if start != '.':
        if tree[start][0]:
            inorder(tree[start][0])
        print(start, end='')
        if tree[start][1]:
            inorder(tree[start][1])
    print()


N = int(input())
alpha = alpha[:N]
tree = {alp: [] for alp in alpha}
for i in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')