while True:
    s = input()
    if not int(s):
        break

    A, B = list(s), reversed(s)
    cnd = True
    for a, b in zip(A, B):
        if a != b:
            print('no')
            cnd = False
            break
    if cnd:
        print('yes')