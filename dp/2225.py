n, k = map(int, input().split())
dp = [[i] * 201 for i in range(201)]

for i in range(1, 201):
    dp[1][i] = i
    dp[i][1] = 1

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[n][k] % 1000000000)