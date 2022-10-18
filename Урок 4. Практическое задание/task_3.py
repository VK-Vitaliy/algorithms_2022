"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return "".join(reversed(str(enter_num)))


entered_num = 12344324567

print(
    f"revers_1 - {timeit('revers_1(entered_num)', setup='from __main__ import revers_1, entered_num', number=10000)}")
print(
    f"revers_2 - {timeit('revers_2(entered_num)', setup='from __main__ import revers_2, entered_num', number=10000)}")
print(
    f"revers_3 - {timeit('revers_3(entered_num)', setup='from __main__ import revers_3, entered_num', number=10000)}")
print(
    f"revers_4 - {timeit('revers_4(entered_num)', setup='from __main__ import revers_4, entered_num', number=10000)}")


'''
Из четырех функций, функция revers_4 использующая срезы оказалась быстрее всех. Полагаю, что в случае со срезами
выполняется значительно меньше вычислительных операций и вызовов, чем в других функциях.
'''