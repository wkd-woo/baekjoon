n = int(input())
l = sorted(map(int, input().split()))
m = int(input())

start, end = 1, l[-1]
result = 0
while start <= end:
    mid = (start + end) // 2  # 중간 값
    temp = 0
    for each in l:
        if each <= mid:
            temp += each
        else:
            temp += mid

    if temp <= m:
        result = max(mid, result)
        start = mid + 1
    elif temp > m:
        end = mid - 1

print(result)