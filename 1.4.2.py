'''
У даному випадку рекурмія займає бцльше пам'яті та може видати помилку, так як досягнеться глибина рекурсії
Код доволі легко читати як в ітераційному так і в рекурсивному методах
'''
import math
from time import time


def prime(number, d=2):
    if number < d:  # числа меньше двох не є простими
        return False
    elif number == d:  # якщо число = 2 воно просте
        return True
    elif number % d == 0:  # послідовне ділення на числа від 2 до d
        return False
    else:
        return prime(number, d + 1)  # рекурсія приякій в ожному наступнуму кроці дільник збільшується на 1


def prime_it(number):
    if number < 2:  # числа меньше двох не є простими
        return False
    if number == 2:  # якщо число = 2 воно просте
        return True
    limit = math.sqrt(number)  # максимальне число на яке може ділитися задане
    i = 2
    while i <= limit:
        if number % i == 0:  # послідовне ділення на числа від 2 до limit
            return False
        i += 1
    return True


number = int(input('enter number'))
if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    print(prime(number))
    toc = time()

else:
    tic = time()
    print(prime_it(number))
    toc = time()

time = toc - tic
print(f'time: {time}')
