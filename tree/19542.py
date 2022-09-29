def inorder(start):
    if start != '.':
        if tree[start][0]:
            inorder(tree[start][0])
        print(start, end='')
        if tree[start][1]:
            inorder(tree[start][1])
    print()