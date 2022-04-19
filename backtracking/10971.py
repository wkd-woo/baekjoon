from itertools import permutations

n = int(input())
g = [list(map(int, input().split())) for i in range(n)]
ans = int(1e9)
l = [i for i in range(n)]

for i in permutations(l, n):
    cost = 0

    for j in range(n):
        if j == n - 1 and g[i[n - 1]][i[0]] != 0:
            cost += g[i[n - 1]][i[0]]
            ans = min(ans, cost)
        elif j != n - 1 and g[i[j]][i[j + 1]] != 0:
            cost += g[i[j]][i[j + 1]]
        else:
            break

print(ans)