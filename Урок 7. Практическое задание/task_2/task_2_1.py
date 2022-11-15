"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
import math

from timeit import timeit


def shell_sort(m):
    array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    median = array[m]
    return median


print(timeit("shell_sort(10)", globals=globals(), number=100))
print(timeit("shell_sort(100)", globals=globals(), number=100))
print(timeit("shell_sort(1000)", globals=globals(), number=100))

"""
Результаты замеров:
0.001962700000149198
0.022597000002861023
0.3334002000046894
"""