n, m = map(int, input().split())
l = list(map(int, input().split()))

left, right = 0, 0
cnt = 0
sum_ = l[left]
while left <= n:
    if sum_ > m:
        sum_ -= l[left]
        left += 1

    elif sum_ < m:
        if right + 1 < n:
            right += 1
            sum_ += l[right]
        else:
            break
    else:
        cnt += 1
        sum_ -= l[left]
        left += 1

print(cnt)
