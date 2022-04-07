import copy

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for i in range(n)]
graph = copy.deepcopy(dp)

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            pass

        elif j == 0:  # 왼쪽 끝
            dp[i][j] = dp[i - 1][j] + graph[i][j]

        elif i == 0:  # 첫 줄
            dp[i][j] = dp[i][j - 1] + graph[i][j]

        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + graph[i][j]

print(dp[n - 1][m - 1])
