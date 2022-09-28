k = int(input())
inorder = list(map(int, input().split()))
for i in range(k):
    for j in range(2 ** i):
        print(inorder[2 ** (k - i - 1) - 1 + 2 ** (k - i) * j], end=' ')
    print()