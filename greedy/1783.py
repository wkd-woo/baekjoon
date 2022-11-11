n, m = map(int, input().split())  # 세로 n 가로 m
x, y = (1, 1)
answer = 1

while (x < m):
    if m - x == 0 or m - x < 2 and n - y < 2:
        break

    if m > 4 and answer < 3:
        x += 2
        if n - y >= 1:
            y += 1
        elif y > 1:
            y -= 1
        else:
            break

    else:
        if m - x > 1 and 0 <= n - y <= 1:  # 두 칸 가야하는 경우
            x += 2
            if n - y == 0:
                y -= 1
            else:
                y += 1

        elif m - x > 0:  # 대부분은 x를 한칸씩 가는게 최선
            x += 1
            if y + 2 > n and y > 2:
                y -= 2
            else:
                y += 2

    answer += 1


print(answer)
