"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""

"""
Задание с курса "Основы языка Python".
Объявляется класс Cart (корзина).
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки 
(объекты классов Table, TV, Notebook и Cup)
"""
from memory_profiler import memory_usage


def decor(func):
    def wrapper():
        m1 = memory_usage()
        func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


# Исходный скрипт
@decor
def func():
    class Cart:
        def __init__(self):
            self.goods = []

        def add(self, gd):
            self.goods.append(gd)

        def remove(self, indx):
            self.goods.pop(indx)

        def get_list(self):
            return [f'{i.name}: {i.price}' for i in self.goods]

    class Table:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class TV:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Notebook:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Cup:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    cart = Cart()
    cart.add(TV('Samsung', 12990))
    cart.add(TV('Sony', 39990))
    cart.add(Table('Решка', 6350))
    cart.add(Notebook('Acer', 35990))
    cart.add(Notebook('Asus', 75990))
    cart.add(Cup('Керамика', 350))


mem_diff = func()
print(f"Выполнение заняло {mem_diff} Mib")


# Оптимизированный скрипт
@decor
def func():
    class Cart:
        def __init__(self):
            self.goods = []

        def add(self, gd):
            self.goods.append(gd)

        def remove(self, indx):
            self.goods.pop(indx)

        def get_list(self):
            return [f'{i.name}: {i.price}' for i in self.goods]

    class Table:
        __slots__ = ["name", "price"]

        def __init__(self, name, price):
            self.name = name
            self.price = price

    class TV:
        __slots__ = ["name", "price"]

        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Notebook:
        __slots__ = ["name", "price"]

        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Cup:
        __slots__ = ["name", "price"]

        def __init__(self, name, price):
            self.name = name
            self.price = price

    cart = Cart()
    cart.add(TV('Samsung', 12990))
    cart.add(TV('Sony', 39990))
    cart.add(Table('Решка', 6350))
    cart.add(Notebook('Acer', 35990))
    cart.add(Notebook('Asus', 75990))
    cart.add(Cup('Керамика', 350))


mem_diff = func()
print(f"Выполнение заняло {mem_diff} Mib")


"""
Аналитика:
Для оптимизации памяти я конструкцию __slots__ при определении классов, 
в результате чего удалось добиться уменьшения расхода памяти
Исходное решение (Выполнение заняло 0.01171875 Mib)
Оптимизированное решение (Выполнение заняло 0.0078125 Mib)
"""