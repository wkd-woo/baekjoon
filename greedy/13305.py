# 현재 주유소가 다음 주유소보다 싼가?
n = int(input())

distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

mn = costs[0]
answer = 0
for i, (distance, cost) in enumerate(zip(distances, costs[1:])):
    answer += distance * mn
    if mn > cost:
        mn = cost

print(answer)
