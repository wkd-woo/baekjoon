n = int(input())
v = [int(input()) for i in range(n)]
dp = [0 for i in range(n + 10000)]

dp[0] = v[0]
if n < 3:
    print(sum(v))
else:
    dp[1] = dp[0] + v[1]
    dp[2] = max(dp[1], dp[0] + v[2], v[1] + v[2])
    if n > 3:
        dp[3] = max(dp[1] + v[3], v[0] + v[2] + v[3], dp[2])
        for i in range(4, n):
            dp[i] = max(dp[i - 3] + v[i - 1] + v[i], dp[i - 2] + v[i], dp[i - 1])
    print(dp[n - 1])