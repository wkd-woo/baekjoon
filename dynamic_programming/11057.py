n = int(input())
dp = [[0] * 10 for i in range(1000 + 1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, 1000 + 1):
    dp[i][0] = dp[i - 1][0]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][3] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
    dp[i][4] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]
    dp[i][5] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]
    dp[i][6] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6]
    dp[i][7] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + \
               dp[i - 1][7]
    dp[i][8] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + \
               dp[i - 1][7] + dp[i - 1][8]
    dp[i][9] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + \
               dp[i - 1][7] + dp[i - 1][8] + dp[i - 1][9]

print(sum(dp[n]) % 10007)
