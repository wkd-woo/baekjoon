from sys import stdin

input = stdin.readline


n, m = map(int, input().split())
l = list(map(int, input().split()))

sum_ = [0 for _ in range(n)]
sum_[0] = l[0]
for i in range(1, n):
    sum_[i] = sum_[i-1] + l[i]

for _ in range(m):
    i, j = map(int, input().split())
    if i - 2 < 0:
        print(sum_[j-1])
    else:
        print(sum_[j-1] - sum_[i-2])
