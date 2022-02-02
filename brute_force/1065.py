number = int(input())


# 한수 여부 확인
def solution(number):
    l = list(map(int, str(number)))
    for i in range(1, len(l)):
        if ((l[0] - l[1]) != (l[1] - l[2])):
            return False

    return True


count = 0
if 1 <= number <= 1000:

    for i in range(1, number + 1):
        if i < 100:
            count += 1
        elif solution(i):
            count += 1

    print(count)
