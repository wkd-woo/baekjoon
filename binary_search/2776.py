def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


t = int(input())

for _ in range(t):
    n = int(input())
    l = sorted(map(int, input().split()))
    m = int(input())
    s = list(map(int, input().split()))
    for each in s:
        print(binary_search(each, l))
