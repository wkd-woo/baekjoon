import sys
import math
from itertools import combinations

input = sys.stdin.readline
INF = float(2e9)


def getDist(ax, ay, bx, by):
    return round(math.sqrt((ax - bx) ** 2 + (ay - by) ** 2), 6)


def dfs(now, bitmask):
    if bitmask | (1 << now) == (1 << n) - 1:
        return graph[now][0] if graph[now][0] != 0 else INF

    if dp[now][bitmask] is not None:
        return dp[now][bitmask]

    cost = INF
    for i in range(n):
        if bitmask & (1 << i) or i == now or graph[now][i] == 0:
            # 모두 방문 or 현재 노드 or 경로가 없는 경우
            continue

        val = dfs(i, bitmask | (1 << i))
        cost = min(cost, val + graph[now][i])

    dp[now][bitmask] = cost
    return cost


n = int(input())
graph = [[0] * n for _ in range(n)]
dp = [[None] * (2**n) for _ in range(n)]

coords = []
for i in range(n):
    x, y = map(int, input().split())
    coords.append((i, x, y))


for A, B in combinations(coords, 2):
    na, ax, ay = A
    nb, bx, by = B
    dist = getDist(ax, ay, bx, by)
    graph[na][nb] = dist
    graph[nb][na] = dist


print(dfs(0, 1))
