n = int(input())
l = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = l[0]

for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + l[i])  # 기존 dp[i]와 dp[j] + l[i] 중 큰 값을 대입
        else:
            dp[i] = max(dp[i], l[i])  # 둘 중 큰 값을 대입

print(max(dp))
