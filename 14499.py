n, m, x, y, k = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
vertical, horizontal = [0, 0, 0, 0], [0, 0, 0, 0]

result = []
for order in orders:
    if order == 4 and x + 1 <= n-1:  # x, n은 세로. 남쪽으로
        print("남쪽")
        x += 1
        vertical = vertical[1:] + [vertical[0]]
        horizontal[1] = vertical[1]
        map_[x][y], vertical[3], horizontal[3] = vertical[3], map_[
            x][y], map_[x][y]
        result.append(vertical[1])

    elif order == 3 and x - 1 >= 0:  # 북쪽으로
        print("북쪽")
        x -= 1
        vertical = [vertical[-1]] + vertical[:3]
        horizontal[1] = vertical[1]
        map_[x][y], vertical[3], horizontal[3] = vertical[3], map_[
            x][y], map_[x][y]
        result.append(vertical[1])

    elif order == 2 and y - 1 >= 0:  # y, m은 가로. 서쪽으로
        print("서쪽")

        y -= 1
        temp = horizontal.pop()
        horizontal = [temp] + horizontal

        map_[x][y], vertical[3], vertical[1], horizontal[3] = vertical[3], map_[
            x][y], horizontal[1], map_[x][y]
        result.append(vertical[1])

        # 좌, 우로 돌릴 때 문제가 있다. 이거 수정해야함
    elif order == 1 and y + 1 <= m-1:  # 동쪽으로
        print("동쪽")
        y += 1
        temp = horizontal.pop(0)
        horizontal = horizontal + [temp]

        map_[x][y], vertical[3], vertical[1], horizontal[3] = vertical[3], map_[
            x][y], horizontal[1], map_[x][y]
        result.append(vertical[1])

    print(vertical, horizontal)
    print(map_)
    print(result)
    print()

for each in result:
    print(each)
