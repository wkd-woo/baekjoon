INF = int(1e9)
n, k = map(int, input().split())
c = [int(input()) for i in range(n)]
c.sort(reverse=True)
dp = [INF] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(c[i], k + 1):
        dp[j] = min(dp[j], dp[j - c[i]] + 1)

print(dp[-1] if dp[-1] != INF else -1)