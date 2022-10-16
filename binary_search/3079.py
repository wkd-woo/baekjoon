from sys import stdin

input = stdin.readline


def solution(n, times):
    start, end = 1, max(times) * n
    while start < end:
        mid = (start + end) // 2
        temp = 0
        for t in times:
            temp += mid // t
        if temp >= n:
            end = mid
        else:
            start = mid + 1
    
    answer = start
    return answer


n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
print(solution(m, times))
