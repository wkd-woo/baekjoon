p = int(input())
change = 1000 - p

cnt = 0
for each in [500, 100, 50, 10, 5, 1]:
    if change // each != 0:
        cnt += change // each
        change = change % each


print(cnt)
