dp = []


def solution(n):  # 반복문
    for i in range(0, n):
        if i == 0:
            dp.append(1)
        elif i == 1:
            dp.append(2)
        else:
            dp.append(dp[i - 1] + dp[i - 2])
    return dp[n - 1]


n = int(input())
print(solution(n) % 10007)

##########################################################

from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def solution2(n):  # 무식한 재귀문
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution2(n - 1) + solution2(n - 2)


n = int(input())
print(solution2(n) % 10007)
