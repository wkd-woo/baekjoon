cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    answer = (V // P) * L + min(L, V % P)

    print("Case {0}: {1}".format(cnt, answer))
