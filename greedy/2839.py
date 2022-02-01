N = int(input())

result = 0
if 3 <= N <= 5000:
    while True:
        if N % 5 == 0:
            result += N // 5
            print(result)
            break
        N -= 3
        result += 1
        if N < 0:
            print(-1)
            break
