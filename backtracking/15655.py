n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

s = []
res = set()


def dfs():
    if len(s) == m:
        res.add(tuple(sorted(s)))
        return

    for i in l:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
for each in sorted(res):
    print(*each)