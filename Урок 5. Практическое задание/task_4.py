"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit

setup_code = """
from collections import OrderedDict
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
"""

change_dict_el = """
r = {'b': 2}
dict_1.pop('b')
dict_1.update(r)
"""
change_ord_dict_el = """
dict_2.move_to_end('b')
"""
print("Меняем элементы местами")
print("dict: ", timeit(setup=setup_code, stmt=change_dict_el, number=10000))
print("OrderedDict: ", timeit(setup=setup_code, stmt=change_ord_dict_el, number=10000))
print("--" * 50)

"""
OrderedDict имеет смысл использовать, если необходимо изменить порядок ключей и поместить какой-то ключ в конец словаря,
эта операция в OrderedDict займет меньше времени и меньший объем кода
"""