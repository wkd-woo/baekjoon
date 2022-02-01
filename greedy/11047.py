def solution(N, K, coins):
    need = 0  # 필요한 동전의 수
    for coin in reversed(coins):
        if K == 0:
            break

        if coin > K:
            pass
        elif K % coin == 0:
            need += K // coin
            K = 0
        elif coin < K:
            n = K // coin
            K -= coin * n
            need += n

    print(need)


def insert(N):
    coins = []  # 동전 종류 리스트

    # 동전 종류 입력 받음
    for i in range(N):
        coin = int(input())
        while i >= 2 and (coin % coins[i - 1] != 0):
            coin = int(input())

        coins.append(coin)
    return coins


# 동전 종류와 만들 금액
N, K = list(map(int, input().split()))

if 1 <= N <= 10 and 1 <= K <= 100000000:
    coins = insert(N)
    solution(N, K, coins)
