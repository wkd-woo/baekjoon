from bisect import bisect_left


n = int(input())
a = list(map(int, input().split()))

lis = [-int(1e9)]
index = [0] * (n + 1)

for i in range(len(a)):
    num = a[i]
    if lis[-1] < num:
        lis.append(num)
        index[i] = len(lis) - 1
    else:
        index[i] = bisect_left(lis, num)
        lis[index[i]] = num

order = len(lis) - 1
print(order)
answer = []
for i in range(n, -1, -1):
    if index[i] == order:
        answer.append(a[i])
        order -= 1

print(*(reversed(answer)))
