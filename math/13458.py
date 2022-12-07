n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
l = [max(0, each-b) for each in a]
result = n
for each in l:
    result += (each // c)
    if each % c != 0:
        result += 1

print(result)
