n = int(input())
dp = [0] * (n + 90)  # DP는 항상 n == 1일 때를 조심

dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    if not dp[i]:
        dp[i] = (dp[i - 1] + dp[i - 2])

print(dp[n])