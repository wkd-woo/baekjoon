T = int(input())


def fibonacci(n):
    if n == 0:
        global zeros
        zeros += 1
        return 0
    elif n == 1:
        global ones
        ones += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(T):
    zeros = 0
    ones = 0
    N = int(input())
    if 0 <= N <= 40:
        fibonacci(N)

    print(zeros, ones)
