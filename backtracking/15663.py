n, m = map(int, input().split())
l = sorted(map(int, input().split()))
visited = [0 for _ in range(n)]
s = list()
res = set()


def dfs(cnt):
    if len(s) == m:
        res.add(tuple(s))
        return

    for i in range(len(l)):
        if not visited[i]:
            visited[i] = 1
            s.append(l[i])
            dfs(i + 1)
            visited[i] = 0
            s.pop()


dfs(0)
for i in sorted(res):
    print(*i)
