"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

setup_code = """
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return list(filter(lambda x: nums[x] % 2 == 0, range(len(nums))))
        

lst_in = [1, 2, 4, 65, 5, 3, 25, 76, 8, 5, 23, 46534, 63, 43, 23, 432, 11]
"""

main_block1 = """
func_1(lst_in)
"""

main_block2 = """
func_2(lst_in)
"""

main_block3 = """
func_3(lst_in)
"""

print("append функция -", timeit(setup=setup_code, stmt=main_block1, number=10000))
print("list comprehension функция -", timeit(setup=setup_code, stmt=main_block2, number=10000))
print("list() + фильтрация через лямбда-функцию -", timeit(setup=setup_code, stmt=main_block3, number=10000))

"""
Функция через list comprehension работает незначительно лучше классического append решения.
Также попробовал вариант использования встроенной функции list с фильтрацией через лямбда-функцию, 
результат почти в 2 раза хуже, чем с функцией append и lc без лямбда
"""


