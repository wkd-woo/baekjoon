n = int(input())
l = list(map(int, input().split()))

dp = [1] * n

# 증가
for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # 기존 dp[i]와 dp[j] + l[i] 중 큰 값을 대입

# 감소
for i in range(1, n):
    for j in range(i):
        if l[i] < l[j]:
            dp[i] = max(dp[i], dp[j] + 1)  # 기존 dp[i]와 dp[j] + l[i] 중 큰 값을 대입

print(max(dp))
