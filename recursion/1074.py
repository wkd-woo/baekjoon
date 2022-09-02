def solution(n, r, c):
    if not n:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * solution(n - 1, r // 2, c // 2)


n, r, c = map(int, input().split())
print(solution(n, r, c))
