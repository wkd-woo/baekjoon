n, m = map(int, input().split())
trees = sorted(map(int, input().split()))

start, end = 0, trees[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    package = 0
    for tree in trees:
        if tree - mid > 0:
            package += tree - mid
        if package >= m:
            break
    if package >= m:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
