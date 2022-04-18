from itertools import permutations
n = int(input())
l = list(map(int, input().split()))
mx = -int(1e9)

for one in permutations(l, n):
    temp = 0
    for i in range(0, n - 1):
        temp += abs(one[i] - one[i + 1])
    mx = max(mx, temp)

print(mx)