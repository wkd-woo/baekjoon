n = int(input())
dp = [i for i in range(n + 10000)]
dp[0] = int(1e9)
dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = min(dp[i], dp[i - 3] + 1)

if dp[n] % 2 == 1:
    print('SK')
else:
    print('CY')