"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
import collections
UsersNums = collections.namedtuple("UsersNums", ["n1", "n2"])
print("Программа сложения и умножения двух шестнадцатеричных чисел")
values = UsersNums(n1=(input("Введите первое число: ")), n2=(input("Введите второе число: ")))
nums1_lst = list(values.n1)
nums2_lst = list(values.n2)
add_res = list(str((hex(int(values.n1, 16) + int(values.n2, 16)))).upper())[2:]
mul_res = list(str((hex(int(values.n1, 16) * int(values.n2, 16)))).upper())[2:]
print(f"Сумма чисел: {add_res}")
print(f"Произведение чисел: {mul_res}")


class HexDigit:
    def __init__(self, dig):
        self.dig = dig

    def __call__(self):
        return list(self.dig)

    def __add__(self, other):
        self.add_hex = hex(int(self.dig, 16) + int(other.dig, 16))
        return list(str(self.add_hex).upper()[2:])

    def __mul__(self, other):
        self.mul_hex = hex(int(self.dig, 16) * int(other.dig, 16))
        return list(str(self.mul_hex).upper()[2:])


n1 = HexDigit("A2")
print(n1())
n2 = HexDigit("C4F")
print(n2())

print(n1 + n2)
print(n1 * n2)
