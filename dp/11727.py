n = int(input())
dp = [0] * (n + 10007)  # DP는 항상 n == 1일 때를 조심

dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
for i in range(5, n + 1):
    if not dp[i]:
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

print(dp[n])