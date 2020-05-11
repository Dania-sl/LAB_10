'''
У даному випадку рекурмія займає бцльше пам'яті
Код доволі легко читати як в ітераційному так і в рекурсивному методах
'''
from time import time


def dig_root(number):
    if number < 10:  # якщо число однозначне то це і буде корінь
        return number
    else:
        return dig_root(
            number // 10 + number % 10)  # рекурсі в якій чило ділиться на 10 для знаходження остачі та додання її та зменшення числа в 10 раз
                                        # і підставлення зменшеного числа в функцію жоки не отримаємо однозначне


def dig_root_it(number):
    if number < 10:  # якщо число однозначне то це і буде корінь
        return number
    else:
        while number > 9:  # виконується до тих пір поки число двузначне
            i = number % 10  # знаходження останьої цифри
            number = number // 10  # число без останьої цифри
            number = number + i  # додання до числа останьої цифри
        return number


number = int(input('enter number'))
if input('if you want to use recursion press Enter, if iteration write something and press Enter: ') == '':
    tic = time()
    print(dig_root(number))
    toc = time()

else:
    tic = time()
    print(dig_root_it(number))
    toc = time()

time = toc - tic
print(f'time: {time}')
