from collections import Counter

N = int(input())
numbers = []

if 1 <= N <= 5000000 and N % 2 == 1:

    for i in range(N):
        temp = int(input())
        if abs(temp) <= 4000:
            numbers.append(temp)

    numbers.sort()

    mean = round(sum(numbers) / len(numbers))
    median = numbers[(len(numbers) // 2)]
    cnt = Counter(numbers).most_common(2)
    if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
        mode = cnt[1][0]
    else:
        mode = cnt[0][0]
    num_range = max(numbers) - min(numbers)

    print(mean)
    print(median)
    print(mode)
    print(num_range)