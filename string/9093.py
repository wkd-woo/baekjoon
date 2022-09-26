for _ in range(int(input())):
    l = input().split()
    l = [w[::-1] for w in l]
    print(' '.join(l))