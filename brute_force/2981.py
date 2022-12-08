n = int(input())
l = list(int(input()) for _ in range(n))
mn = min(l)  # O(1)
answer = []
for i in range(mn):  # O(1bil)
    temp = [each - i for each in l]  # O(100)
