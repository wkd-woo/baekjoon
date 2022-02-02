N = int(input())

count = 0

if 1 <= N <= 10 ** 6:
    loop = True
    while loop:
        if N == 1:
            loop = False
            break

        if (N - 1) % 3 == 0:
            count += 1
            if N // 2 >= 10:
                N -= 1
                N = N // 3
                count += 1
            else:
                N = N // 2
        elif N % 3 == 0 and N // 2 > 10:
            N = N // 3
            count += 1
        elif N % 3 == 0 and N // 2 <= 10:
            N = N // 2
            count += 1
        elif N % 2 == 0 and (N - 1) % 3 != 0:
            N = N // 2
            count += 1
        else:
            N -= 1
            count += 1
        print(N)

    print(count)
