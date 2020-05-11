'''
У даному випадку рекурмія займає бцльше пам'яті так як весь стек визовів збирігається
Код доволі легко читати як в ітераційному так і в рекурсивному методах
'''
import random
import numpy as np
from time import time


def maximum(arr, column=0, row=0, i=0, j=0):
    if row == len(arr[column]):
        column += 1
        row = 0
    if column == len(arr):
        return arr[i][j]
    if arr[column][row] > arr[i][j]:
        i = column
        j = row
    row += 1
    return maximum(arr, column, row, i, j)


def maximum_it(arr, max_num=0):
    for i in range(len(arr)):  # номер рядку
        for j in range(len(arr)):  # номер стовбчику
            if max_num < arr[i][j]:  # порівння
                max_num = arr[i][j]  # якщо елемент більший він запишеться у змінну
    return max_num


n = int(input('Enter size array: '))
arr = np.zeros((n, n))  # створення нульового масиву заданої розмірності
for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][j] = random.randint(1, 20)  # заповнення масиву
print(arr)
if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    print(maximum(arr))
    toc = time()

else:
    tic = time()
    print(maximum_it(arr))
    toc = time()

time = toc - tic
print(f'time: {time}')
