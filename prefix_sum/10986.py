n, m = map(int, input().split())
l = list(map(int, input().split()))

sum_ = [0 for _ in range(n)]
sum_[0] = l[0]
for i in range(1, n):
    sum_[i] = sum_[i-1] + l[i]

cnt = 0
for each in l:
    if each % m == 0:
        cnt += 1

for i in range(n):
    sum_[i] = sum_[i] % m

sum_2 = [0 for _ in range(n)]
sum_2[0] = sum_[0]
for i in range(1, n):
    sum_2[i] = sum_2[i-1] + sum_[i]

for i in range(n):
    sum_2[i] = sum_2[i] % m

cnt += sum_.count(0) + sum_2.count(0)
print(cnt)
print(sum_)
print(sum_2)
