'''
У даному випадку рекурмія займає бцльше пам'яті та може видати помилку, так як досягнеться глибина рекурсії
Код доволі легко читати як в ітераційному так і в рекурсивному методах
'''
from time import time


def factorial(number):
    if number == 0:  # якщо число = 0 то факторыал буде 1
        return 1
    else:
        return number * factorial(
            number - 1)  # рекурсія множимо число на число перед ним, та визиваємо знову функцію але з значенням меньше на 1


def factorial_it(number, factorial=1):
    while number > 1:
        factorial *= number  # множимо задане чило на число перд ним
        number -= 1  # віднімаємо 1 від поточного числа для знаходження попереднього
    return factorial


number = int(input('enter number: '))
if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    print(factorial(number))
    toc = time()

else:
    tic = time()
    print(factorial_it(number))
    toc = time()

time = toc - tic
print(f'time: {time}')

