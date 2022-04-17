n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

s = []


def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in l:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()