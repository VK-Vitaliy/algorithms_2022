"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from timeit import timeit

setup_code = """
from collections import deque
lst_in = [i for i in range(1000000)]
deq_in = deque(lst_in)
def return_el(ls, x):
    return ls[x]
"""

lst_append = """
lst_in.append(1)
"""
deque_append = """
deq_in.append(1)
"""
print("Метод append")
print("lst.append: ", timeit(setup=setup_code, stmt=lst_append, number=10000))
print("deque.append: ", timeit(setup=setup_code, stmt=deque_append, number=10000))
print("--" * 50)
lst_pop = """
lst_in.pop()
"""
deque_pop = """
deq_in.pop()
"""
print("Метод pop")
print("lst.pop: ", timeit(setup=setup_code, stmt=lst_pop, number=10000))
print("deque.pop: ", timeit(setup=setup_code, stmt=deque_pop, number=10000))
print("--" * 50)

lst_extend = """
lst_in.extend(["Leopard", "Lynx"])
"""
deque_extend = """
deq_in.extend(["Leopard", "Lynx"])
"""
print("Метод extend")
print("lst.extend: ", timeit(setup=setup_code, stmt=lst_extend, number=10000))
print("deque.extend: ", timeit(setup=setup_code, stmt=deque_extend, number=10000))
print("--" * 50)

lst_appendleft = """
lst_in.insert(0, 3)
"""
deque_appendleft = """
deq_in.appendleft(3)
"""
print("Метод insert(0) и appendleft")
print("lst.insert: ", timeit(setup=setup_code, stmt=lst_appendleft, number=10000))
print("deque.appendleft: ", timeit(setup=setup_code, stmt=deque_appendleft, number=10000))
print("--" * 50)

lst_popleft = """
lst_in.pop(0)
"""
deque_popleft = """
deq_in.popleft()
"""
print("Метод pop(0) и apopleft")
print("lst.pop(0): ", timeit(setup=setup_code, stmt=lst_popleft, number=10000))
print("deque.popleft: ", timeit(setup=setup_code, stmt=deque_popleft, number=10000))
print("--" * 50)

lst_extendleft = """
new_ext = ["Leopard", "Lynx"]
lst_in = lst_in[::-1] + new_ext[::-1]
lst_in = lst_in[::-1]
"""
deque_extendleft = """
deq_in.extendleft(["Leopard", "Lynx"])
"""
print("Метод extendleft")
print("lst.extendleft: ", timeit(setup=setup_code, stmt=lst_extendleft, number=1000))
print("deque.extendleft: ", timeit(setup=setup_code, stmt=deque_extendleft, number=1000))
print("--" * 50)

lst_return_el = """
return_el(lst_in, 50)
"""
deque_return_el = """
return_el(deq_in, 50)
"""
print("Получение элемента")
print("lst: ", timeit(setup=setup_code, stmt=lst_return_el, number=1000))
print("deque: ", timeit(setup=setup_code, stmt=deque_return_el, number=1000))
print("--" * 50)

"""
ВЫВОДЫ:
1) операции append, extend списка и дек у небольних массивов показывают примерно равные результаты, 
но при увеличении массива дек начинает уступать списку, метод pop показывает одинаковые результаты.
2) дек показывает очень хорошие результаты с операциями appendleft, popleft, extendleft и работает значительно быстрее.
3) получение элемента выполняется быстрее в обычном списке 
"""

