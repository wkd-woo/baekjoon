n = int(input())
l = list(map(int, input().split()))

cnt = 0
l.sort()
for i, first in enumerate(l):
    l = [each - first for each in l]
    del l[i]
    left, right = 0, len(l)-1
    while left < right:
        sum_ = l[left] + l[right]
        if sum_ == 0:
            cnt += 1
            left += 1
        elif sum_ > 0:
            right -= 1
        else:
            left += 1

    l = [each + first for each in l]
    l.insert(i, first)

for i, first in enumerate(l):
    l = [each - first for each in l]
    del l[i]
    left, right = 0, len(l)-1
    while left < right:
        sum_ = l[left] + l[right]
        if sum_ == 0:
            cnt += 1
            right -= 1
        elif sum_ > 0:
            right -= 1
        else:
            left += 1

    l = [each + first for each in l]
    l.insert(i, first)

if n < 3:
    print(0)
else:
    print(cnt//2)
