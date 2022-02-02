i = 0

T = int(input())
while i < T:

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    rm = abs(r1 - r2)
    rp = r1 + r2

    i += 1
    if distance == 0:
        if rm == 0:
            print(-1)
        else:
            print(0)
    else:
        if distance < rp and distance > rm:
            print(2)
        elif distance == rp or distance == rm:
            print(1)
        else:
            print(0)
else:
    pass
