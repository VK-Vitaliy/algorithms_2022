"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

import heapq


def is_leaf(root):
    return root.left is None and root.right is None


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(root, s, huffman_code):
    if root is None:
        return

    if is_leaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else "1"

    encode(root.left, s + "0", huffman_code)
    encode(root.right, s + "1", huffman_code)


def bilding_huffman_tree(text: str):
    if len(text) == 0:
        return
    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]

    heapq.heapify(pq)

    while len(pq) != 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        total = left.freq + right.freq
        heapq.heappush(pq, Node(None, total, left, right))

    root = pq[0]
    huffman_code = {}
    encode(root, "", huffman_code)
    print('Кодовая таблица символов:', huffman_code)
    print('Оригинальная строка:', text)
    s = ''
    for c in text:
        s += huffman_code.get(c)
    print('Закодированное сообщение:', s)


text = "hello python!"

bilding_huffman_tree(text)
