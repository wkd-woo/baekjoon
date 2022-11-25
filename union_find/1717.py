import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent, edges = [i for i in range(0, n + 1)], []
for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        union(a, b)

    if order == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
