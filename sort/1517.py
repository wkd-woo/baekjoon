n = int(input())
l = list(map(int, input().split()))


def bubble_sort(arr):
    start = 0
    end = len(arr) - 1
    cnt, order = 0, sorted(arr, reverse=True)
    while start < end:
        if order and order[-1] == arr[start]:
            start += 1
            order.pop()

        last_swap = 0
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
                cnt += 1

        end = last_swap

    return cnt


print(bubble_sort(l))
