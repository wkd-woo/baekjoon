import itertools

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    if 0 < N <= M < 30:
        print(len(list(itertools.combinations(range(M), N))))
