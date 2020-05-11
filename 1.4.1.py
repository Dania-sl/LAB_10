'''
У даному випадку рекурмія займає бцльше пам'яті та може видати помилку, так як досягнеться глибина рекурсії
Код простіше читається у ітераційному варфанті
'''
from time import time


def rev(arr):
    if not arr:#якщо списук пустий поверне його
        return []
    else:
        return [arr[-1]] + rev(arr[:-1])#рекурсыя яка кожного разу обрізає список до останього елемену і додає його у спимок


def rev_it(arr):
    return arr[::-1]#зріз списку у зворотньому напрямі


arr = []
while True:
    number = input('Enter number: ')
    if number != '':
        arr.append(int(number))
    else:
        break


if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    a = rev(arr)
    a.append('.')
    print(a)
    toc = time()

else:
    tic = time()
    b = rev_it(arr)
    b.append('.')
    print(b)
    toc = time()

time = toc - tic
print(f'time: {time}')
