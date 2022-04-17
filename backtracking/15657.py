n, m = map(int, input().split())
l = sorted(map(int, input().split()))

s = []
res = set()


def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in l:
        if len(s) == 0 or s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()

dfs()