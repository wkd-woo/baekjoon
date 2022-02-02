N = int(input())

l = list(map(int, input().split()))
numbers = [each for each in l if -1000000 <= each <=1000000]
if 1<= N <= 1000000:
    print(min(numbers), max(numbers))