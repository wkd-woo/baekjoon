t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n + 100)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        if not dp[i]:
            dp[i] = (dp[i - 2] + dp[i - 3])

    print(dp[n])