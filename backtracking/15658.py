n = int(input())
a = list(map(int, input().split()))
opers = list(map(int, input().split()))
mx = -int(1e9)
mn = int(1e9)


def dfs(idx, ans):
    global mx, mn

    if idx == n:
        mx = max(mx, ans)
        mn = min(mn, ans)
        return

    if opers[0] > 0:
        opers[0] -= 1
        dfs(idx + 1, ans + a[idx])
        opers[0] += 1
    if opers[1] > 0:
        opers[1] -= 1
        dfs(idx + 1, ans - a[idx])
        opers[1] += 1
    if opers[2] > 0:
        opers[2] -= 1
        dfs(idx + 1, ans * a[idx])
        opers[2] += 1
    if opers[3] > 0:
        opers[3] -= 1
        dfs(idx + 1, int(ans / a[idx]))
        opers[3] += 1


dfs(1, a[0])
print(mx)
print(mn)