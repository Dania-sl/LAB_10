'''
У даному випадку рекурмія займає бцльше пам'яті та може видати помилку, так як досягнеться глибина рекурсії
Код простіше читається у ітераційному варіанті
'''
from time import time


def trans(number, sys=16):
    if not hasattr(trans, 'table'):  # перевырка чи є в trans обєкт з table
        trans.table = '0123456789ABCDEF'  # задаємо таблицю значень шістнадцятирічної системи
    x, y = divmod(number, sys)  # за допомогою цього методу знаходимо остачу ти ціле число від ділення
    return trans(x, sys) + trans.table[y] if x else trans.table[y]


def trans_it(number, sys=16):
    trans_it.table = '0123456789ABCDEF'  # задаємо тфблицю значень шістнадцятирічної системи
    r = ''
    while number:
        number, y = divmod(number, sys)  # за допомогою цього методу знаходимо остачу ти ціле число від ділення
        r = trans_it.table[y] + r  #
    return r


number = int(input('enter number'))
if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    print(trans(number))
    toc = time()

else:
    tic = time()
    print(trans_it(number))
    toc = time()

time = toc - tic
print(f'time: {time}')
