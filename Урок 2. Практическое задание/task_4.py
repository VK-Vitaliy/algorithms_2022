"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def adding_numbers(n, sum_numbers=0, start_num=1):
    if n == 0:
        return sum_numbers
    else:
        sum_numbers += start_num
        start_num = start_num / -2
        n -= 1
        return adding_numbers(n, sum_numbers, start_num)


print(adding_numbers(int(input('Введите количество элементов: '))))
