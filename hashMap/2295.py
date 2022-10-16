from sys import stdin

input = stdin.readline


def solution(l):
    answer = -int(1e9)
    for j in range(len(l)-1, -1, -1):
        target = l[j]
        for i, each in enumerate(l):
            l = [temp - each for temp in l]
            start, end = 0, len(l)-1
            while start <= end:
                sum_ = l[start] + l[end]
                if sum_ == target:
                    answer = target
                    return answer
                elif sum_ < target:
                    start += 1
                else:
                    end -= 1

            l = [temp + each for temp in l]


n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
print(solution(l))
