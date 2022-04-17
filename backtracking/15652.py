n, m = map(int, input().split())
l = []


def dfs(x, y):
    if x == m:
        print(*l)
        return
    for i in range(y, n):
        l.append(i + 1)
        dfs(x + 1, i)
        l.pop()


dfs(0, 0)