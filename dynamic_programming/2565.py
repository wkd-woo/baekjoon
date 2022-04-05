n = int(input())
dp = [0] * n
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

l.sort()
dp = [1] * n
for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))