import numpy as np

row, column = map(int, input().split())

array = []

before = 0
now = 0
wrong = 0

for i in range(row):
    array[i] = list(input())
    before = array[j][0].copy()

    for j in range(1, column):
        now = array[i][j].copy()
        if now == before:
            wrong += 1
        before = now.copy()
