t = int(input())

for _ in range(t):
    cnt, word = input().split()
    cnt, word, s = int(cnt), list(word), ''

    for w in word:
        s = s + cnt * w

    print(s)