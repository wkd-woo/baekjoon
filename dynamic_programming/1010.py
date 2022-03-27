import math

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    # result = M!/(M - N)!(N!)
    result = math.factorial(M) // (math.factorial(M - N) * math.factorial(N))
    print(result)
