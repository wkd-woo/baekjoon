import re

def chk_digit(l):
    if l[0].isdigit() and l[-1].isdigit():
        return True
    else:
        return False


line = input()
operator = re.findall("[^0-9]", line)

if len(line) <= 50:
    l = list((line.replace('+', ' + ').replace('-', ' - ')).split())

    if chk_digit(l):
        result = 0
        condition = False

        for i, each in enumerate(l):
            if len(each) <= 5:
                if each.isnumeric() and not condition:
                    result += int(each)
                elif each == '-':
                    condition = ~condition
                elif each.isnumeric() and condition:
                    result -= int(each)
                else:
                    pass

    print(result)
