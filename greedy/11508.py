N = int(input())
C = []
result = 0

for i in range(N):
    C.append(int(input()))

if 1 <= N <= 100000 and all(1 <= x <= 100000 for x in C):
    l = sorted(C)
    for i, each in enumerate(reversed(l)):
        if (i + 1) % 3 == 0:
            pass
        else:
            result += each
    print(result)