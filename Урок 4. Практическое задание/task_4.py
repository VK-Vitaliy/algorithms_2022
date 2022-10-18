"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1, 3, 3]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    ar_dict = {}
    for i in array:
        if i in ar_dict:
            ar_dict[i] += 1
        else:
            ar_dict[i] = 1
    for i, j in ar_dict.items():
        if j == max(ar_dict.values()):
            return f'Чаще всего встречается число {i}, ' \
                   f'оно появилось в массиве {max(ar_dict.values())} раз(а)'


def func_4():
    res = Counter(array).most_common(1)
    return f'Чаще всего встречается число {res[0][0]}, ' \
           f'оно появилось в массиве {res[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(
    f"func_1 - {timeit('func_1()', setup='from __main__ import func_1', number=10000)}")
print(
    f"func_2 - {timeit('func_2()', setup='from __main__ import func_2', number=10000)}")
print(
    f"func_3 - {timeit('func_3()', setup='from __main__ import func_3', number=10000)}")
print(
    f"func_4 - {timeit('func_4()', setup='from __main__ import func_4', number=10000)}")


"""
Первый вариант классического цикла с условием оказался самый быстрый, решения с использованием стандартных функций 
и библиотек python показывает более худшие результаты.
"""