def solution(n):
    def hanoi(n, From, Toward, Sub):
        if n == 1:
            answer.append([From, Toward])
            return
        hanoi(n-1, From, Sub, Toward)
        answer.append([From, Toward])
        hanoi(n-1, Sub, Toward, From)

    answer = []
    hanoi(n, 1, 3, 2)
    print(len(answer))
    for ans in answer:
        print(*ans)

    return answer


n = int(input())
solution(n)
