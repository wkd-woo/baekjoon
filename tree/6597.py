def buildTree(preorder, inorder):
    if inorder:
        # 전위순회에서 node = pop()하여 루트 정함
        node = preorder.pop()
        index = inorder.index(node)
        tree[node][0] = buildTree(preorder, inorder[0:index])
        tree[node][1] = buildTree(preorder, inorder[index + 1:])

        return node


def postorder(start):
    if start:
        if tree[start][0]:
            postorder(tree[start][0])
        if tree[start][1]:
            postorder(tree[start][1])
        print(start, end='')


while True:
    try:
        preorder, inorder = input().split()  # 전위순회
        preorder, inorder = list(preorder), list(inorder)
        preorder.reverse()
        tree = {each: [0, 0] for each in inorder}
        root = buildTree(preorder, inorder)
        postorder(root)
        print()
    except:
        break