n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

s = []
res = set()


def dfs():
    if len(s) == m:
        res.add(tuple(s))
        return

    for i in l:
        if len(s) != m:
            s.append(i)
            dfs()
            s.pop()


dfs()
for each in sorted(res):
    print(*each)