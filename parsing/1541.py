import re


def chk_digit(l):
    for i in range(1, len(l)):
        if (l[i - 1].isdigit() and l[i].isdigit()) or (not l[i - 1].isdigit() and not l[i].isdigit()):
            return False
    return True


def chk_first_last(l):
    if not l[0].isdigit() and not l[-1].isdigit():
        return False
    return True


line = input()
operator = re.findall("[^0-9]", line)
pattern = re.compile("^[0-9] + [0-9]\-\+ + [0-9]$")

if pattern:
    l = list((line.replace('+', ' + ').replace('-', ' - ')).split())
    if chk_digit(l) and chk_first_last(l):
        result = 0
        condition = False

        for i, each in enumerate(l):

            if each.isnumeric() and not condition:
                result += int(each)
            elif each == '-':
                condition = ~condition
            elif each.isnumeric() and condition:
                result -= int(each)
            else:
                pass

        print(result)
