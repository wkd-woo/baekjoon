condition = True

while condition:
    A, B = map(int, input().split())

    if 0 < A < 10 and 0 < B < 10:
        condition = False
        print(A / B)
    else:
        pass
