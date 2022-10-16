n = int(input())
l = list(map(int, input().split()))
x = int(input())

l.sort()
left, right = 0, n - 1
cnt = 0
while left < right:
    sum_ = l[left] + l[right]
    if sum_ == x:
        cnt += 1
        left += 1
    elif sum_ > x:
        right -= 1
    else:
        left += 1

print(cnt)
