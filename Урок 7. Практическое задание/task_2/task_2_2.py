"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def find_median(m):
    array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    for i in range(m):
        array.remove(max(array))
    return max(array)


print(timeit("find_median(10)", globals=globals(), number=100))
print(timeit("find_median(100)", globals=globals(), number=100))
print(timeit("find_median(1000)", globals=globals(), number=100))

"""
Результаты замеров:
0.0013221999979577959
0.025667399997473694
1.7396555000013905
"""