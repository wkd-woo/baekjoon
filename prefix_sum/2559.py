n, k = map(int, input().split())
l = list(map(int, input().split()))

sum_ = [0 for _ in range(n)]
sum_[0] = l[0]
for i in range(1, n):
    sum_[i] = sum_[i-1] + l[i]

mx = sum(l[:k])
for i in range(n):
    if i + k >= n:
        break
    else:
        mx = max(sum_[i+k] - sum_[i], mx)

print(mx)
