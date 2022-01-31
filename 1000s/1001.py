condition = True

try:
    while condition:
        A, B = map(int, input().split())

        if 0 < A < 10 and 0 < B < 10:
            condition = False
            print(A - B)
        else:
            pass
except ValueError:
    print('정수를 입력해주세요')
