n, c = map(int, input().split())
l = sorted(int(input()) for _ in range(n))

start = 1 - l[0]
end = l[-1] - l[0]
result = 0

while (start <= end):
    mid = (start + end) // 2  # 중간 값
    value = l[0]
    cnt = 1
    for i in range(1, len(l)):
        if l[i] >= value + mid:  # l[i]가 값 + 중간 갭을 더한 것 보다 크면
            value = l[i]
            cnt += 1
    if cnt >= c:  # 설치할 수 있는 공유기가 C보다 많거나 같다면
        start = mid + 1  # 최대 갭 올림
        result = mid  # 갭 지정
    else:  # 설치할 수 있는 공유기가 C보다 적으면
        end = mid - 1

print(result)
