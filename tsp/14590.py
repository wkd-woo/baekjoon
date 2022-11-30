import sys

input = sys.stdin.readline
INF = int(2e9)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[None] * (2**n) for _ in range(n)]
path = []


def dfs(now, bitmask):
    path.append(now)

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
