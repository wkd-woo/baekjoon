while True:
    a, b, c = sorted(map(int, input().split()))
    if a == b == c == 0:
        break
    a, b, c = a**2, b**2, c**2
    if a + b == c:
        print("right")
    else:
        print("wrong")
