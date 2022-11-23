k = int(input())

pos = []
for i in range(6):
    d, w = map(int, input().split())
    pos.append(w)


mx, mn = 0, 0
for i in range(6):
    temp = pos[i] * pos[(i+1) % 6]
    if mx < temp:
        mx = temp
        idx = i

mn = pos[(idx + 3) % 6] * pos[(idx + 4) % 6]
print(k * (mx - mn))
