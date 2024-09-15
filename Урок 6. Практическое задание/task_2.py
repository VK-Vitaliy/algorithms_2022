"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

"""
Если выполнить профилирование памяти к рекурсивной функции декоратор profile будет срабатывать каждый раз,
когда вызывается рекурсивная функция внутри себя.
Вывод: Профилирование рекурсии удобно выполнять когда она находится внутри другой функции   
"""

from memory_profiler import profile


def calculated_even_odd(number, even=0, odd=0):
    if number < 10:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        if (number % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return calculated_even_odd(number // 10, even, odd)


@profile
def recursion2(n):
    def calculated_even_odd(number, even=0, odd=0):
        if number < 10:
            if number % 2 == 0:
                even += 1
            else:
                odd += 1
            print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
        else:
            if (number % 10) % 2 == 0:
                even += 1
            else:
                odd += 1
            return calculated_even_odd(number // 10, even, odd)

    calculated_even_odd(n)


recursion2(1010111)


