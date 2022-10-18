from bisect import bisect_left


n = int(input())
l = list(map(int, input().split()))

lis = []
for i, each in enumerate(l):
    if i == 0:
        lis.append(each)
        continue
    if lis[-1] > each:
        idx = bisect_left(lis, each)
        lis[idx] = each
    elif lis[-1] < each:
        lis.append(each)


print(len(lis))
