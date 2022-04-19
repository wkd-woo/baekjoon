n = int(input())
l = [i for i in range(1, n + 1)]
s = []


def dfs():
    if len(s) == n:
        print(*s)
        return

    for i in l:
        if len(s) == 0 or i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
