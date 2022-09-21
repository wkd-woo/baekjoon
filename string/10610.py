n = list(sorted(map(int, input()), reverse=True))

if n[-1] != 0 or sum(n) % 3 != 0:
    print(-1)
else:
    print(''.join(map(str, n)))
