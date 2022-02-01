try:
    N = int(input())
    P = list(map(int, input().split()))

    if 1 <= N <= 1000 and all(1 <= x <= 1000 for x in P):
        min_list = sorted(P)
        result = 0

        for i in range(1, N + 1):
            result += sum(min_list[:i])

        print(result)
except IndexError:
    pass
