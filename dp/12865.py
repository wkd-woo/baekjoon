n, k = map(int, input().split())  # n: 물품의 수 k: 최대무게

weights = []
values = []
for i in range(n):  # w: 물건의 무게, v: 물건의 가격
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0 for i in range(k + 1)] for i in range(n + 1)]

for i in range(n + 1):
    for w in range(k + 1):
        if i == 0 or w == 0:  # 물건이 0일 때 - 배낭이 0일 때
            dp[i][w] = 0

        elif weights[i - 1] <= w:  # 물건을 챙길 수 있을 때
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])  # 가격비교

        else:
            dp[i][w] = dp[i - 1][w]

print(dp[n][k])
