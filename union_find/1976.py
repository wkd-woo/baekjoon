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


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)


l = list(map(int, input().split()))

result = []
for each in l:
    result.append(find(each - 1))

print("YES") if len(set(result)) == 1 else print("NO")
