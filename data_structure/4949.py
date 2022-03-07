match_dict = {']': '[', ')': '('}


def solution(s):
    stack = []
    for each in s:
        if each == '(' or each == '[':
            stack.append(each)
        elif each == ')' or each == ']':
            if len(stack) == 0 or stack[len(stack) - 1] != match_dict[each]:
                return False
            stack.pop()
    if len(stack) != 0:
        return False

    return True


while True:
    s = input()

    if s == '.':
        break

    if solution(s):
        print('yes')
    else:
        print('no')