from sys import stdin
import math

input = stdin.readline


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


start, end = map(int, input().split())
l = list(range(start, end+1))
answer = [number for number in l if is_prime_number(number)]
answer.sort()
for num in answer:
    print(num)
