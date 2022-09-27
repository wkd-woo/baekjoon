import sys
sys.setrecursionlimit(10 ** 6)

preordered = []
while True:
    try:
        preordered.append(int(sys.stdin.readline()))
    except:
        break

def postOrder(start, end):
    if start > end:
        return

    root = preordered[start]
    i = start + 1

    while i <= end:
        if preordered[i] > root:
            break # 루트보다 크면 넘긴다
        i += 1

    postOrder(start + 1, i - 1)
    postOrder(i, end) # 루트 오른쪽에서 순회
    print(root)

postOrder(0, len(preordered)-1)