"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
from os import urandom

url_cache = dict()


class UrlCache:
    SALT = urandom(16)

    def __init__(self):
        self.__url_cache = dict()

    def check_cache(self, url: str):
        return self.__url_cache.setdefault(url, hashlib.sha512(self.SALT + url.encode('utf-8')).hexdigest())

    @property
    def url_cache(self):
        return self.__url_cache


cache = UrlCache()
cache.check_cache('https://gb.ru/')
cache.check_cache('https://gb.ru/')
cache.check_cache('https://stepik.org/learn')
cache.check_cache('https://lms.metaclass.kts.studio/courses')
print(cache.url_cache)

