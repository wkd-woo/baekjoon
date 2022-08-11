k, n = map(int, input().split())
l = sorted(int(input()) for _ in range(k))
start, end = 1, l[-1]
result = 0
while start <= end:
    mid = (start + end) // 2  # 중간 값
    cnt = 0
    for each in l:
        cnt += each // mid

    if cnt >= n:
        result = max(mid, result)
        start = mid + 1
    elif cnt < n:
        end = mid - 1

print(result)